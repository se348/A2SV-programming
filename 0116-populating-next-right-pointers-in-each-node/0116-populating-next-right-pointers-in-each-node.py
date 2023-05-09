"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        diction = defaultdict(list)
        
        def dfs(curr, ind):
            if not curr:
                return
            diction[ind].append(curr)
            dfs(curr.left, ind + 1)
            dfs(curr.right, ind + 1)
        
        dfs(root, 0)
        for i in diction:
            for j in range(len(diction[i]) -1):
                diction[i][j].next = diction[i][j + 1]
        
        return root;