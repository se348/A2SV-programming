class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        if target < nums[0]:
            return 0

        res= math.inf
        
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
                
            elif target < nums[mid]:
                res = min(res, mid)
                right = mid -1
            
            else:
                return mid
        if res == math.inf:
            return len(nums)
        return res 
            