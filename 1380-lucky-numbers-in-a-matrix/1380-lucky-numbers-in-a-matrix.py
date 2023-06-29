class Solution:
    def minimRows(self, matrix):
        vals = set()
        
        for i in range(len(matrix)):
            temp = 0
            for j in range(1, len(matrix[0])):
                if matrix[i][j] < matrix[i][temp]:
                    temp = j 
            vals.add((i, temp))
        
        return vals
    
    def maximCols(self, matrix):
        vals = set()
        
        for i in range(len(matrix[0])):
            temp = 0
            
            for j in range(1, len(matrix)):
                if matrix[j][i] > matrix[temp][i]:
                    temp = j
                    
            vals.add((temp, i))
        
        return vals
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
            minRows = self.minimRows(matrix)
            maximCols = self.maximCols(matrix)
            temp = minRows.intersection(maximCols)
            res = []
            
            for i,j in temp:
                res.append(matrix[i][j])
            return res
        
        