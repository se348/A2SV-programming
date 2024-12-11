class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        min_number = nums[0]
        max_number = nums[-1]
        
        res = 0
        
        for curr_number in range(min_number, max_number + 1):
            min_val = curr_number - k
            max_val = curr_number + k
            
            res = max(res, bisect_right(nums, max_val) - bisect_left(nums, min_val))
            
        return res
            