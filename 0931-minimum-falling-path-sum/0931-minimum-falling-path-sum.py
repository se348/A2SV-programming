class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for i in range(n -2 , -1, -1):
            for j in range(n):
                temp = matrix[i + 1][j]
                if j > 0:
                    temp = min(temp, matrix[i + 1][j - 1])
                if j < n - 1:
                    temp = min(temp, matrix[i + 1][j + 1])
                    
                matrix[i][j] += temp 
        
        return min(matrix[0])