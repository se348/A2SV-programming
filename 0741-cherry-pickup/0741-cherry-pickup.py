class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        dirs = [[1, 0], [0, 1]]
        
        @cache
        def dfs(i1, i2, j1, j2):
            nonlocal n, m
            
            if i1 >= n or i2 >= n:
                return -inf
            
            if j1 >= m or j2 >= m:
                return -inf
            
            if grid[i1][j1] == -1 or grid[i2][j2] == -1:
                # print(i1, j2, i2, j2)
                return -inf
            
            if i1 == i2 == n - 1 and j1 == j2 == m - 1:
                return grid[i1][j1]
            
            curr = -inf
            for a_x, a_y in dirs:
                for b_x, b_y in dirs:
                    c1 = i1 + a_x
                    c2 = i2 + b_x
                    
                    d1 = j1 + a_y
                    d2 = j2 + b_y
                    
                    curr = max(curr, dfs( c1, c2, d1, d2))
            
            if i1 == i2 and j1 == j2:
                
                return curr + grid[i1][j1]
            
            
            return curr + grid[i1][j1] + grid[i2][j2]
        
        t = dfs(0,0,0,0)
        
        return t if t != -inf else 0
            
            