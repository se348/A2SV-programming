# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        
        def dfs(curr, path):
            nonlocal total
            path.append(str(curr.val))
            
            if not curr.left and not curr.right:
                total += int("".join(path))
            
            if curr.left:
                dfs(curr.left, path)
                
            if curr.right:
                dfs(curr.right, path)
                
            path.pop()
                
        dfs(root, [])
        return total