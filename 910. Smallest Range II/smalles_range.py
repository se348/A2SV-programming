from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        soln = nums[-1] - nums[0]
        
        for i in range(len(nums)-1):
            min_val = min(nums[0]+k, nums[i+1]-k)
            max_val = max(nums[i]+k, nums[-1]-k)
            soln = min(soln, max_val-min_val)
            
        return soln  
            
                
