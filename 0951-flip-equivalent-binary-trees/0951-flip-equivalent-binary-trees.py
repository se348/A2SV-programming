# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def count(node):
            if not node:
                return 0
            
            res = 1
            res += count(node.left)
            res += count(node.right)
            return res
        def dfs(curr_1 , curr_2):
            if not curr_1.left and not curr_1.right:
                if not curr_2.left and not curr_2.right:
                    return True
                return False

            if not curr_2.left and not curr_2.right:
                return False
            
            option1 = True
            
            if curr_1.left:
                if curr_2.left and curr_1.left.val == curr_2.left.val:
                    option1 = option1 and dfs(curr_1.left, curr_2.left)
                elif curr_2.right and curr_1.left.val == curr_2.right.val:
                    option1 = option1 and dfs(curr_1.left, curr_2.right)
                else:
                    return False
            if curr_1.right:
                if curr_2.left and curr_1.right.val == curr_2.left.val:
                    option1 = option1 and dfs(curr_1.right, curr_2.left)
                elif curr_2.right and curr_1.right.val == curr_2.right.val:
                    option1 = option1 and dfs(curr_1.right, curr_2.right)
                else:
                    return False
            return option1
        

        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        c1, c2 = count(root1), count(root2)
        if c1 != c2:
            return False
        if root1.val == root2.val:
            return dfs(root1, root2)