class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        def compute():
            curr_sum = 0
            maxim = 0

            for i in range(len(nums)):
                curr_sum += nums[i]

                if curr_sum < 0:
                    curr_sum = 0

                maxim = max(curr_sum, maxim)
            return maxim
        
        a = compute()
        
        for i in range(len(nums)):
            nums[i] *= -1
        
        b=compute()
        
        return max(a, b)