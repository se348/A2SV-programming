# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        largest = defaultdict(lambda: -inf)
        
        def findLargest(level, node):
            if not node:
                return
            
            largest[level] = max(largest[level], node.val)
            
            findLargest(level + 1, node.left)
            findLargest(level + 1, node.right)
            
        findLargest(0, root)
        
        res = [0] * len(largest)
        
        for key in largest:
            res[key] = largest[key]
        
        return res
        