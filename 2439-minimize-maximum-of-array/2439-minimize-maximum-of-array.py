class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n= len(nums)
        
        total = 0
        maxim = nums[0]
        
        for i in range(n):
            total += nums[i]
            
            maxim = max(maxim, ceil(total / (i + 1)))
        
        return maxim


            
        