from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum=0
        res= 0
        prefix_sum= {0:1}
        for num in nums:
            curr_sum+=num
            if curr_sum -k in prefix_sum:
                res+= prefix_sum[curr_sum -k]
            prefix_sum[curr_sum] =1+ prefix_sum.get(curr_sum, 0)
        return res