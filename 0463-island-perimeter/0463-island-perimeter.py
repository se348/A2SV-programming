class Solution:
    def findNeighbor(self, grid, curr_x, curr_y):
        count = 0
        if curr_x == 0:
            count += 1
        if curr_y == 0:
            count += 1
        if curr_x == len(grid) - 1:
            count += 1
        if curr_y == len(grid[0]) -1:
            count += 1
        if curr_x > 0 and grid[curr_x - 1][curr_y]==0:
            count += 1
        if curr_y > 0 and grid[curr_x][curr_y - 1]==0:
            count += 1
        if curr_x < len(grid) -1 and grid[curr_x + 1][curr_y] == 0:
            count += 1
        if curr_y < len(grid[0]) - 1 and grid[curr_x][curr_y + 1] == 0:
            count += 1
        return count
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 1:
                    continue
                perimeter += self.findNeighbor(grid, i, j)
        
        return perimeter