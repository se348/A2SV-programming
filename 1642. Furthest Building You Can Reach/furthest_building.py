import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        custom_heap =[]
        for i in range(len(heights) -1):
            if heights[i] < heights[i+1]:
                heapq.heappush(custom_heap,heights[i+1] -heights[i])
                if len(custom_heap) > ladders:
                    bricks -= heapq.heappop(custom_heap)
                    if bricks <0:
                        return i
        return len(heights) - 1
        