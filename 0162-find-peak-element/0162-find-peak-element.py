class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        
        if length == 1:
            return 0
        
        if nums[0]> nums[1]:
            return 0
        
        if nums[length -2] < nums[length -1]:
            return length -1
        
        left = 1
        right = length -2
        
        while left <= right:
            mid = (left + right) //2
            
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid + 1]:
                return mid
            
            elif nums[mid] < nums[mid -1]:
                right = mid -1
            
            else:
                left = mid + 1
        
        return 0