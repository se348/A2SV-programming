class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = max(nums[i], 0)
            
        left_ptr = 0
        
        for right_ptr in range(len(nums)):
            if nums[right_ptr] == 0:
                continue
            
            while left_ptr < right_ptr and nums[left_ptr] != 0:
                left_ptr += 1
                
            if nums[left_ptr] == 0:
                nums[right_ptr], nums[left_ptr] = nums[left_ptr], nums[right_ptr]
        
        min_val = inf
        for i in range(left_ptr + 1):
            min_val = min(min_val, abs(nums[i]))
        
        if min_val != 1:
            return 1
        
        for i in range(left_ptr + 1):
            curr_num = abs(nums[i]) - 1
            
            if curr_num <= left_ptr:
                nums[curr_num] = abs(nums[curr_num]) * -1
        
        for i in range(len(nums)):
            if nums[i] >= 0:
                return (i + 1)
        return len(nums) + 1
            