class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        dirs = [[1, 0], [1, -1], [1, 1]]
        
        @cache
        def dfs(i1, j1, j2):
            if i1 == len(grid):
                return 0
            
            if (j1 < 0) or (j2 < 0) or (j1 >= len(grid[0])) or j2 >= len(grid[0]):
                return 0
            
            curr =0
            
            for dir_x, dir_y in dirs:
                for a, b in dirs:
                    
                    g =  min(j1 + dir_y, j2 + b)
                    h = max( j1 + dir_y, j2 + b)
                    
                    curr = max(curr, dfs(i1 + 1,g,h))
            
            if j1 == j2:
                return curr + grid[i1][j1]    
            
            return curr + grid[i1][j1] + grid[i1][j2]
        
        return dfs(0, 0, len(grid[0]) - 1)
            
            