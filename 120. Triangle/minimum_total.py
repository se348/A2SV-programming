from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo={}
        def dfs(row, column):
            if (row,column) in memo:
                return memo[(row,column)]
            if row>=len(triangle):
                return 0
            left_res= dfs(row+1, column)
            right_res= dfs(row+1, column+1)
            memo[(row,column)] =min(left_res, right_res)+ triangle[row][column]
            return min(left_res, right_res)+ triangle[row][column]
        return dfs(0,0)
            