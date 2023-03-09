from itertools import accumulate

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        length =  len(nums)
        prefix = [0] * (length + 1)
        
        for i, j in requests:
            prefix[i] += 1
            prefix[j + 1] -= 1
        
        pref_sum = list(accumulate(prefix))
        nums.sort()
        pref_sum.pop()
        pref_sum.sort()
        res = 0
        
        for i in range(len(nums)):
            res += (nums[i] * pref_sum[i])
            
        return res % (10 **9 + 7)