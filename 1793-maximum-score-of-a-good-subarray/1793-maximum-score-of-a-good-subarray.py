class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        monotonic_stack = []
        length = len(nums)
        left_extreme = [0] * length
        
        for i in range(length):
            while monotonic_stack and nums[i] <= nums[monotonic_stack[-1]]:
                monotonic_stack.pop()
                
            monotonic_stack.append(i)
            
            if len(monotonic_stack) == 1:
                left_extreme[i] = -1
            else:
                left_extreme[i] = monotonic_stack[-2]
        
        right_extreme = [0] * length
        monotonic_stack = []
        
        for i in range(length -1, -1, -1):
            while monotonic_stack and nums[i] <= nums[monotonic_stack[-1]]:
                monotonic_stack.pop()
                
            monotonic_stack.append(i)
            
            if len(monotonic_stack) == 1:
                right_extreme[i] = length
            else:
                right_extreme[i] = monotonic_stack[-2]
        
        res = 0
        for i in range(length):
            left = i - left_extreme[i] - 1
            right = right_extreme[i] - i - 1 
            if (i - left) <= k <=(i + right):
    
                res = max(res, ((right + i) - (i - left) + 1) * nums[i])
        return res