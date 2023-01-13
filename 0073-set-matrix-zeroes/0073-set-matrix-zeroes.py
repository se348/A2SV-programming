class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()
        
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                
                if matrix[row][column] == 0:
                    rows.add(row)
                    columns.add(column)
                    
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                
                if row in rows or column in columns:
                    
                    matrix[row][column] = 0
                    
                    