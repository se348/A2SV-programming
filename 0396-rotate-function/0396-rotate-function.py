class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total  = sum(nums)
        
        current_res = 0 
        length = len(nums)
        
        for i in range(length):
            current_res += (i * nums[i])
            
        maxim_res =  current_res
        
        current_index = length - 1
        
        for i in range(length):
            current_res += total - nums[current_index]
            current_res -= (length - 1) * nums[current_index]
            
            current_index -= 1
            maxim_res = max(maxim_res, current_res)
        
        return maxim_res
        