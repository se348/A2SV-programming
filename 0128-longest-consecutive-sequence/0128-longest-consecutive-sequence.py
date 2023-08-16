class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        prev = -math.inf
        count = 0
        
        for i in range(n):
            
            if nums[i] - prev == 1:
                
                count += 1
                
            elif nums[i] != prev:
                count = 1 
            
            res = max(res, count)
            prev = nums[i]
            
        return res
