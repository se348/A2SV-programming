class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        prev = -101
        
        for right in range(len(nums)):
            
            if nums[right] == prev:
                continue

            prev = nums[right]
            nums[right] , nums[left] = nums[left], nums[right]
            left += 1
        
        
        return left
