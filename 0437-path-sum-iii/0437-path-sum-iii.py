# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        
        def checkSum(root, accum):
            nonlocal count
            if not root:
                return
            
            accum += root.val
            count += prefixSum[accum - targetSum]
            prefixSum[accum] += 1
            
            checkSum(root.left, accum)
            checkSum(root.right, accum)
            
            prefixSum[accum] -=1
            
        checkSum(root, 0)
        return count
            