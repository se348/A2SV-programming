class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        tot, n = sum(nums), len((nums))
        if tot == x:
            return n
        target = tot - x
        left_ptr, res = 0, -1
        
        curr_sum = 0
        for right_ptr in range(n):
            curr_sum += nums[right_ptr]
            
            while curr_sum > target and left_ptr<right_ptr:
                curr_sum -= nums[left_ptr]
                left_ptr += 1
            if curr_sum == target:
                res= max(res, right_ptr -left_ptr + 1)
                
        return n - res if res != -1 else -1