class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        memo = {}
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        inbound = lambda x,y: 0 <= x < m and 0 <= y < n
        
        def dfs(row, col, remaining):
            
            if not inbound(row, col):
                return 1
            
            if remaining == 0:
                return 0
            
            if (row, col, remaining) in memo:
                return memo[(row, col, remaining)]
            
            count = 0
            
            for dir_x, dir_y in directions:
                
                next_row = row + dir_x
                next_col = col + dir_y
                
                count += dfs(next_row, next_col, remaining - 1)
                
            memo[(row, col, remaining)] =  count
            return count
        
        return (dfs(startRow, startColumn, maxMove) % ((10 ** 9) + 7))