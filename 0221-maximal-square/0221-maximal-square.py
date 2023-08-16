class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix[0])
        n = len(matrix)
        
        res= 0
        maxim = [[0 for _ in range(m)] for _ in range(n)]
        
        
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                curr_val = matrix[i][j]
                
                if matrix[i][j] == "0":
                    continue
                right_val, diagonal_val, down_val = 0, 0, 0
                
                if j < m -1:
                    right_val = maxim[i][j + 1]
                    
                if j < m -1 and i < n - 1:
                    diagonal_val = maxim[i + 1][j + 1]
                
                if i < n - 1:
                    down_val = maxim[i + 1][j]
                    
                maxim[i][j] = min(right_val, diagonal_val, down_val) + 1
                res = max(res, maxim[i][j])
        
        print(maxim)
        return pow(res, 2)
                
                    
                