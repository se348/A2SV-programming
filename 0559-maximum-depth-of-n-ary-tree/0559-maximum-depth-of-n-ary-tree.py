"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(curr):
            if not curr:
                return 0
            
            max_res = 0
            for i in curr.children:
                max_res = max(max_res, dfs(i))
            
            return max_res + 1
        
        return dfs(root)