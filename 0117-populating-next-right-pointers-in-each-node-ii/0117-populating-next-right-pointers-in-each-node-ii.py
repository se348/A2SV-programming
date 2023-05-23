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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque()
        queue.append((root, 0))

        prev, prevLevel = None, 0

        while queue:
            curr, level = queue.popleft()
            
            if prev and prevLevel == level:
                prev.next = curr
            
            if curr.left:
                queue.append((curr.left, level + 1))
            if curr.right:
                queue.append((curr.right, level + 1))
                
            prev = curr
            prevLevel = level
            
        return root
             
                     

