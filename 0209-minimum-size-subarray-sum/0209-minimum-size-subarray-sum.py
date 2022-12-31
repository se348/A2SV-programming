class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        slow_ptr = 0
        length = math.inf
        curr_sum = 0
        
        for fast_ptr in range(len(nums)):
            
            if nums[fast_ptr] + curr_sum >= target:
                length = min(length , fast_ptr - slow_ptr + 1)
                curr_sum += nums[fast_ptr] 
                
                while curr_sum >= target:
                    length = min(length , fast_ptr - slow_ptr + 1)
                    curr_sum -= nums[slow_ptr]
                    slow_ptr += 1
                    
            else: curr_sum += nums[fast_ptr]
        
        if length == math.inf:
            return 0
        return length
                    