class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        start = 0
        count= 0
        
        curr_diff = nums[1] - nums[0]
        
        
        for i in range(1, len(nums)):
            
            if curr_diff == nums[i] - nums[i- 1]:
                count += max(0, i - start - 1)
            else:
                curr_diff = nums[i] - nums[i - 1]
                start = i - 1
        
        
        return count
    
