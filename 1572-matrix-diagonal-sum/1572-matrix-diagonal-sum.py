class Solution:
    def diagonalSum(self, matrix: List[List[int]]) -> int:
        total = 0
        
        for i in range(len(matrix)):
            total += matrix[i][i]
            
            if i != len(matrix) - i- 1:            
                total += matrix[i][len(matrix) -i -1]
            
        return total