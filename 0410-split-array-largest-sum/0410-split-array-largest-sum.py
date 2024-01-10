class Solution:
    def is_achievable(self, nums, max_sum, k):
        curr_sum = 0
        res = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            
            if curr_sum > max_sum:
                curr_sum = nums[i]
                res += 1
            
        return res < k
                
            
        
    def splitArray(self, nums: List[int], k: int) -> int:
        
        right = sum(nums)
        left = max(nums)
        
        res = -1
        while left <= right:
            
            mid = (left + right) // 2
            
            
            if self.is_achievable(nums, mid, k):
                res = mid
                right = mid - 1
            
            else:
                left = mid + 1
                
        return res