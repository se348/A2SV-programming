# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = None
        
        def dfs(node):
            nonlocal ans
            if not node:
                return (False, False)
            if ans:
                return (False, False)
            
            a, b = dfs(node.left)
            c, d = dfs(node.right)
            
            left, right = a or c, b or d
            
            if node == p:
                left = True
            if node == q:
                right = True
            
            if left and right and not ans:
                ans = node
            
            return (left, right)
        
        dfs(root)
        return ans
            