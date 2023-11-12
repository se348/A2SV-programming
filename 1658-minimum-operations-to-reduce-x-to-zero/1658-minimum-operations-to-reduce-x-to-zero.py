class Solution:
    def minOperations(self, nums, x: int) -> int:
        length = len(nums)
        curr_sum = 0
        target = sum(nums) - x
        left_ptr = 0
        max_window = 0
        if target == 0:
            return length
        for right_ptr in range(length):
            curr_sum += nums[right_ptr]
            
            while left_ptr <= right_ptr and curr_sum > target:
                curr_sum -= nums[left_ptr]
                left_ptr += 1
            
            if curr_sum ==  target:
                max_window = max(max_window, right_ptr - left_ptr + 1)
        
        if not max_window:
            return -1
        res = length - max_window
        return res
                
            