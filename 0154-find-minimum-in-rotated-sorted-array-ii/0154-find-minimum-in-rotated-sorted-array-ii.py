class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        mid = 0
        value = float('inf')
        
        while low <= high:
            mid = (low + high )// 2
            value = min(value, nums[mid])
            
            if nums[low] >= nums[mid] and nums[mid] > nums[high]:
                low = mid + 1
            elif nums[low] < nums[mid] and nums[mid] <= nums[high]:
                high = mid - 1
            elif nums[low] <= nums[mid] and nums[mid] > nums[high]:
                low = mid + 1
            else:
                left, right = mid - 1, mid + 1
                while left >= 0 and right < len(nums) and nums[left] == nums[right]:
                    left -= 1
                    right += 1
                if left >= 0 and right < len(nums) and nums[left] < nums[right]:
                    high = mid - 1
                else:
                    low = mid + 1
        
        return value
    
    