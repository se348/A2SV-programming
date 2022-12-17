from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        prefix = [[0 for i in range(len(grid[0])+1)] for j in range(len(grid)+1)]
        for i in range(len(grid)):
            tempo= 0
            for j in range(len(grid[0])):
                prefix[i+1][j+1] = grid[i][j] + tempo
                tempo =prefix[i+1][j+1]
        res= 0 
        for i in range(1, len(prefix)-2):
            for j in range(1, len(prefix[0])-2):
                res= max(res, prefix[i][j+2] - prefix[i][j-1] + grid[i][j] +prefix[i+2][j+2] - prefix[i+2][j-1])
        return res