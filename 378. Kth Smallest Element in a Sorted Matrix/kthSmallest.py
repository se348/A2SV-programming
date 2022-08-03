import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row =0
        solumn =0
        custom_heap =[]
        for i in range(len(matrix)):
            heapq.heappush(custom_heap, (matrix[0][i], 0, i))
        
        for i in range(k):
            elem , row, column = heapq.heappop(custom_heap)
            if (row+1 < len(matrix)):
                heapq.heappush(custom_heap, (matrix[row+1][column], row +1, column))
        return elem
