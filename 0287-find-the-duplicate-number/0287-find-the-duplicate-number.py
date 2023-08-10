class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            positive = abs(nums[i])
            if nums[positive] < 0:
                return positive
            nums[positive] = -abs(nums[positive])