class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            number = abs(nums[i])
            if nums[number - 1] < 0:
                return number
            nums[number - 1] *= -1