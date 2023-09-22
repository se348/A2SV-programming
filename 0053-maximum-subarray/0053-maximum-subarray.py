class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_tot = 0
        result = min(nums)
        
        for i in range(len(nums)):
            if curr_tot < 0:
                curr_tot = 0
            curr_tot +=  nums[i]
            result = max(result, curr_tot)
        
        return result
            