# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, nums, left, right):
        if left > right or right <left:
            return None
        elif left == right:
            return TreeNode(nums[left])
        
        mid = (left + right) //2
        right_tree = self.dfs(nums, mid +1, right)
        left_tree = self.dfs(nums, left , mid -1)
        
        curr = TreeNode(nums[mid])
        curr.right = right_tree
        curr.left = left_tree
        
        return curr
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.dfs(nums, 0, len(nums) -1)