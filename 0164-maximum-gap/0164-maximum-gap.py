class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        nums.sort()
        
        res= -1
        
        for i in range(len(nums) - 1):
            res = max(res, nums[i + 1]- nums[i])
        
        return res