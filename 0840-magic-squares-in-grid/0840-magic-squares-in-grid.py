class Solution:
    def isMagicSquare(self, grid ,row, col):
        rows =[0 for i in range(3)]
        cols =[0 for j in range(3)]
        diagonal1 = 0
        diagonal2 = 0
        seta = set()
       
                
        for i in range(3):
            for j in range(3):
                rows[i]+= grid[row + i][col + j]
                cols[j]+= grid[row + i][col + j]
                if i==j:
                    diagonal1 += grid[row + i][col + j]
                if i + j == 2:
                    diagonal2 += grid[row + i][col + j]
                seta.add(grid[row + i][col + j])
        if len(seta) != 9 or min(seta)!= 1 or max(seta)!=9 :
            return False
        row_sum = rows[0]
        for i in rows:
            if row_sum != i:
                return False
        
        col_sum = rows[0]
        for j in cols:
            if col_sum != j:
                return False
            
        if row_sum != col_sum:
            return False
        
        if diagonal1 != diagonal2 or diagonal1 != row_sum: return False
        return True
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                if self.isMagicSquare(grid, row, col):
                    count += 1
                    
        return count