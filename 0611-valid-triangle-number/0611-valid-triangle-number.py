class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        combinations = 0
        nums.sort()
        for pivot in range(len(nums)-1,-1,-1):
            
            right = pivot -1
            left = 0
            
            while left < right:
                
                if nums[left] + nums[right] > nums[pivot]:
                    
                    combinations += (right -left)
                    right -= 1
                    
                else:
                    left += 1
                    
        return combinations