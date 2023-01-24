class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        
        while right < len(nums):
            
            if nums[left] != 0:
                
                left += 1
                right = max(right, left)
            
                
            elif nums[right] == 0:
                
                right += 1
                
            else:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                right += 1
                