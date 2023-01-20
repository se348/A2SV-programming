class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        start = (len(grid) * len(grid[0]) - k) % (len(grid) * len(grid[0]))
        
        result = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        end = len(grid) * len(grid[0]) -1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result[i][j] = grid[start // len(grid[0])][start % len(grid[0])]
                if start == end:
                    start = 0 
                else:
                    start += 1
        
        return result
        