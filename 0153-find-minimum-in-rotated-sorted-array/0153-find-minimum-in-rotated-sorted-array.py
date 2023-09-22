class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        
        if nums[0] <= nums[length - 1]:
            return nums[0]
        
        if length <= 2:
            if nums[0] > nums[length - 1]:
                return nums[length - 1]
            return nums[0]
        
        left = 0
        right = length - 1
        
        while left < right:
            mid = ceil((left + right) / 2)
            
            if mid == left + 1 and nums[mid] <= nums[left]:
                return nums[mid]
            elif nums[mid] >= nums[left]:
                left = mid 
            else:
                right = mid