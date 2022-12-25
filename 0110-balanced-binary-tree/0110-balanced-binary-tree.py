# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr:
                return 0, True
            left, isLeftBalanced = dfs(curr.left)
            right, isRightBalanced = dfs(curr.right)
            if abs(left -right) <=1 and isLeftBalanced and isRightBalanced:
                return max(left, right)+1, True
            else:
                return max(left, right)+1, False
        return dfs(root)[1]