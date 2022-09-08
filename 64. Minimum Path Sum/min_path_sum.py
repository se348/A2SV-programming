import math
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo ={}
        def dfs(m,n):
            if (m,n) in memo:
                return memo[(m,n)]
            if len(grid)-1==m and len(grid[0])-1==n:
                return grid[m][n]
            if len(grid)<=m:
                return math.inf
            if len(grid[0])<=n:
                return math.inf
            right =dfs(m,n+1)
            down= dfs(m+1,n)
            memo[(m,n)] = min(right, down) + grid[m][n]
            return min(right, down) + grid[m][n]
        ans= dfs(0,0)
        return ans