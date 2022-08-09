
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    ans= 0
    def maxDepth(self, root: 'Node') -> int:
        if root:
            self.helper(root)
        return self.ans
    
    
    def helper(self, node, curr=0):
        if node.children:
            for n in node.children:
                self.helper(n, curr+1)
        else:
            self.ans= max(self.ans, curr+1)
        