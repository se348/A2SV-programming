class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        initial = 0
        
        for i in range(len(nums)):
            initial = initial ^ nums[i]
        
        return initial