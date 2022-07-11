import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new_nums =[]
        for n in nums:
            new_nums.append(-1 * n)
        heapq.heapify(new_nums)
        for n in range(k):
            a =heapq.heappop(new_nums)
        return -1 * a