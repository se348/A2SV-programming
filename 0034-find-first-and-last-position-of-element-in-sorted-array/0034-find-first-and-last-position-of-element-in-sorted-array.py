class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        idx =0
        left= 0 
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                idx = mid
                break
                
            elif nums[mid] > target:
                right = mid -1
                
            else:
                left = mid + 1
        
        if not nums or nums[idx] != target:
            return [-1, -1]
        
        left =idx
        while left>=0 and nums[left] == target:
            left -= 1
        
        right =idx
        while right < len(nums) and nums[right] == target:
            right += 1
        
        return [left +1, right -1]