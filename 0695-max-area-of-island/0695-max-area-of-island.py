class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        inbound = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited and grid[x][y] == 1
        
        def dfs(x, y):
            
            visited.add((x, y))
            
            count = 1
            
            for i, j in directions:
                curr_x = x + i
                curr_y = y + j
                
                if inbound(curr_x, curr_y):
                    count += dfs(curr_x, curr_y)
            
            return count
        
        max_area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
                    
        return max_area