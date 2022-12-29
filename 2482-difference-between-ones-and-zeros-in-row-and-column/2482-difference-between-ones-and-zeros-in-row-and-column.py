class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        row_ones= [0 for i in range(len(grid))]
        column_ones = [0 for j in range(len(grid[0]))]
        row_zeros= [0 for i in range(len(grid))]
        column_zeros = [0 for j in range(len(grid[0]))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row_ones[i] += 1
                    column_ones[j] += 1
                else:
                    row_zeros[i] += 1
                    column_zeros[j] +=1
                
        res= [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        
        row_len = len(grid[0])
        col_len = len(grid)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                res[i][j] = row_ones[i] + column_ones[j] - row_zeros[i] - column_zeros[j]
            
        
        
        return res