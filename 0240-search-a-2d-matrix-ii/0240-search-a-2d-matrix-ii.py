class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        
        for idx in range(len(nums)):
            val = 0
            
            left = 0
            right = len(nums[0]) - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[idx][mid] == target:
                    return True
                
                elif nums[idx][mid] < target:
                    left = mid + 1
                
                else:
                    right = mid -1
        return False
    