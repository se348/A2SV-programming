class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        
        min_res = inf
        
        for i in range(len(nums) - 1):
            min_res = min(nums[i + 1]- nums[i], min_res)
            
        return min_res