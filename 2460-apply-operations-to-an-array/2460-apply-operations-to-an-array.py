class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        index = 0
        
        while index < len(nums) - 1:
            
            if nums[index] == nums[index +1]:
                nums[index] *= 2
                nums[index+1] = 0
                index += 2
                
            else:
                index += 1
                
        left_ptr = 0
        right_ptr = 1
        
        while right_ptr < len(nums):
            
            if nums[right_ptr] == 0 or right_ptr == left_ptr:
                right_ptr += 1

            elif nums[left_ptr] != 0:
                left_ptr += 1
                
            else:
                nums[left_ptr], nums[right_ptr] = nums[right_ptr] , nums[left_ptr]
                left_ptr += 1
                right_ptr += 1
        
        return nums
            