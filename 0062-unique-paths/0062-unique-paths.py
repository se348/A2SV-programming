class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}
        def dfs(row,col):
            if (row,col) in memo:
                return memo[(row,col)]
            if row==m and col==n:
                return 1
            if row==m:
                return 1
            if col==n:
                return 1
            a= dfs(row+1,col)
            b =dfs(row,col+1)
            memo[(row,col)] =a+b
            return a+b
        return dfs(1,1)