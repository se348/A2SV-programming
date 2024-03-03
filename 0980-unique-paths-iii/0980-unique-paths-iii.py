class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        isValid = lambda x,y: 0 <= x < len(grid) and  0<= y < len(grid[0]) and grid[x][y] != -1
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def backtrack(curr_x, curr_y, must_visit):
            
            if grid[curr_x][curr_y] == 2:
                if must_visit != 1:
                    return 0
                return 1
            
            count = 0
            
            for dir_x, dir_y in directions:
                
                if not isValid(curr_x + dir_x, curr_y + dir_y):
                    continue
                
                prev = grid[curr_x][curr_y]
                
                grid[curr_x][curr_y] = -1
                count += backtrack(curr_x + dir_x, curr_y + dir_y, must_visit - 1)
                grid[curr_x][curr_y] = prev
                
            return count
        
        obstacles_count = 0
        pos = None
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    pos = (i, j)
                elif grid[i][j] == -1:
                    obstacles_count +=1
        
        must_visit = (len(grid) * len(grid[0])) - obstacles_count
        return backtrack(pos[0], pos[1],  must_visit)