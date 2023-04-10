# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(curr):
            if curr and not curr.left and not curr.right:
                return 1
            
            left, right = math.inf, math.inf
            
            if curr.left:
                left= dfs(curr.left)
            if curr.right:
                right = dfs(curr.right)
                
            temp =min(left, right)
            return 1 + temp
        if not root:
            return 0
        return dfs(root)