class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        isRowDeletable = False
        isColumnDeletable = False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                isRowDeletable = True
                
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                isColumnDeletable = True

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                
                if matrix[row][column] == 0:
                    matrix[row][0] = 0
                    matrix[0][column] = 0

        for row in range(len(matrix)-1,0,-1):
            for column in range(len(matrix[0])-1,0,-1):

                if matrix[row][0] == 0 or matrix[0][column] == 0:
                    
                    matrix[row][column] = 0
        
        if isRowDeletable:
            for row in range(len(matrix)):
                matrix[row][0] = 0
        
        if isColumnDeletable:
            for column in range(len(matrix[0])):
                matrix[0][column] = 0
        
        