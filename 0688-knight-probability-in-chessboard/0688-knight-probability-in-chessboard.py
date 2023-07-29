class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        moves = [[1, 2], [2, 1], [-1, 2], [-2, 1], [-1, -2], [-2,-1], [1,-2], [2,-1]]   
        memo = {}
        
        def backtrack(curr_row, curr_col, remaining_k):
            if curr_row >= n or curr_col >= n or curr_row<0 or curr_col <0:
                return 0
            
            if not remaining_k:
                return 1
            if (curr_row, curr_col, remaining_k) in memo:
                return memo[(curr_row, curr_col, remaining_k)]
                
            result = 0
            
            for move in moves:
                result += backtrack(curr_row + move[0], curr_col + move[1], remaining_k -1)
            memo[(curr_row, curr_col, remaining_k)] = (result / 8)
            return memo[(curr_row, curr_col, remaining_k)]
        
        return backtrack(row, column, k)