# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(left, right):
            if left == right:
                return TreeNode(preorder[left])
            
            left_child_stop = -1
            
            for ind in range(left +1, right +1):
                if preorder[ind] < preorder[left]:
                    left_child_stop = ind
            
            curr = TreeNode(preorder[left])
            
            if left_child_stop == -1:
                curr.left = None
                curr.right = dfs(left +1, right)
            
            elif left_child_stop == right:
                curr.left = dfs(left +1, right)
                curr.right =None
                
            else:
                curr.left = dfs(left +1, left_child_stop)
                curr.right = dfs(left_child_stop + 1, right)
                
            return curr
        
        return dfs(0, len(preorder) -1)