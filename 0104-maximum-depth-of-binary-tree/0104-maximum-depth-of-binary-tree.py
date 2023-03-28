# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        length = 1
        
        while stack:
            
            curr, ind = stack.pop()
            
            length =max(length , ind)
            
            if curr.left:
                stack.append((curr.left, ind + 1))
                
            if curr.right:
                stack.append((curr.right, ind + 1))
        
        return length