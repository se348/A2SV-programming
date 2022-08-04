import heapq
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        heapq.heapify(nums)
        while sum(nums) !=  0:
            val = heapq.heappop(nums)
            if val==0: continue
            for i in range(len(nums)):
                nums[i] -= val
            count+=1
        return count