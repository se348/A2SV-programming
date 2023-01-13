class Solution:
    def findMaxVal(self, x, y, grid):
        return max(grid[x][y],grid[x+1][y], grid[x+2][y],
                  grid[x][y+1],grid[x+1][y+1], grid[x+2][y+1],
                  grid[x][y+2],grid[x+1][y+2], grid[x+2][y+2])
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result =[[0 for i in range(len(grid[0])-2)] for j in range(len(grid)-2)]
        
        for x in range(len(grid)-2):
            for y in range(len(grid[0])-2):
                result[x][y] = self.findMaxVal(x,y,grid)
                
        return result