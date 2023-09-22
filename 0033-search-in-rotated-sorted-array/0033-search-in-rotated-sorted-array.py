class Solution:
    def findSmallest(self, nums):
        length = len(nums)
        if nums[0] < nums[length - 1]:
            return 0
        if length <= 2:
            if nums[0] <= nums[length - 1]:
                return 0
            return length - 1
        
        left = 0
        right = length - 1
        
        while left < right:
            mid = ceil((left + right)/ 2)
            
            if mid == left + 1 and nums[mid] < nums[left]:
                return mid
            
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
                
    def binarySearch(self, left, right, target, nums):
        while left <= right:
            mid = (left + right)// 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1      
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        minim = self.findSmallest(nums)
        length = len(nums)
        if nums[minim] <= target <= nums[length - 1]:
            return self.binarySearch(minim, length -1, target, nums)
        
        elif nums[0] <= target:
            return self.binarySearch(0, minim, target, nums)

        else: return -1