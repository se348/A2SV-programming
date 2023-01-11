class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left , right =0 ,0
        
        while right < len(nums):
            
            if nums[left] != 0 and left < right:
                left +=1
                
            elif nums[right] == 0:
                right+=1
                
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right +=1