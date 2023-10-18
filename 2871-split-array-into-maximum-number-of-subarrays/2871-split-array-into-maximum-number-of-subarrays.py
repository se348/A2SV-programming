class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        total_and = nums[0]
        
        for i in range(1, len(nums)):
            total_and = total_and & nums[i]
            
        if total_and != 0:
            return 1
        
        count = 0
        current = nums[0]
        
        for i in range(len(nums)- 1):
            current =current & nums[i]
            if current == 0:
                count += 1
                current = nums[i + 1]
                
        if current & nums[-1] == 0:
            count += 1
        return count