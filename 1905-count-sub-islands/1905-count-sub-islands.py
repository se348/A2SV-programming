class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        inbound = lambda x,y:  0<=x <len(grid2) and 0<=y < len(grid2[0]) and grid2[x][y]
        
        
        cond = True
        def dfs(r, c):
            nonlocal cond
            if not grid1[r][c]:    
                cond = False
            
            for dir_x, dir_y in directions:
                next_x, next_y =dir_x + r, dir_y + c
                
                if inbound(next_x, next_y):
                    
                    grid2[next_x][next_y] = 0

                    dfs(next_x, next_y)
        
        res =0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                
                if not grid2[i][j]:
                    continue
                    
                cond = True
                grid2[i][j] = 0
                dfs(i, j)
                if cond:
                    res +=1
                        
        return res