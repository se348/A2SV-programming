class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}
        def dp(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            
            if row ==len(matrix) - 1:
                value = matrix[row][col]
                return value
            
            option1, option3 = inf, inf
            if col >=1:
                option1= dp(row +1, col -1)
            option2 =dp(row + 1, col)
            if col < len(matrix[0]) -1:
                option3 =dp(row + 1, col + 1)
            
            memo[(row, col)] = min(option1, option2, option3) + matrix[row][col]
            return memo[(row, col)]
        
        min_res = inf
        
        for i in range(len(matrix[0])):
            min_res = min(dp(0, i), min_res)
        return min_res