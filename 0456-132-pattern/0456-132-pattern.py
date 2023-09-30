class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        monotonic_stack = [(nums[0], nums[0])]
        
        min_value = inf
        
        for i in range(1, len(nums)):
            
            while monotonic_stack and monotonic_stack[-1][0] <= nums[i]:
                a, b = monotonic_stack.pop()
                min_value = min(b, min_value)
                
            min_value = min(min_value, nums[i])
            if monotonic_stack and monotonic_stack[-1][0]> nums[i] > monotonic_stack[-1][1]:
                return True
            
            monotonic_stack.append((nums[i], min_value))
            
        return False