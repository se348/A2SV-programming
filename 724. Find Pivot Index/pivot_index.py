from typing import List 
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum =sum(nums)
        sum_up_to_now =0
        for i, n in enumerate(nums):
            total_sum-=n
            if sum_up_to_now==total_sum:
                return i
            sum_up_to_now+= n
        return -1
