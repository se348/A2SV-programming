class Solution:
    def totalNQueens(self, n: int) -> int:
        used_rows = set()
        used_cols = set()
        used_diag_1 = set()
        used_diag_2 = set()
        
        
        def dfs(curr_row, curr_col):
            used_rows.add(curr_row)
            used_cols.add(curr_col)
            used_diag_1.add(curr_row + curr_col)
            used_diag_2.add(curr_row - curr_col)
            
            if curr_row == n -1:
                used_rows.remove(curr_row)
                used_cols.remove(curr_col)
                used_diag_1.remove(curr_row + curr_col)
                used_diag_2.remove(curr_row - curr_col)
                
                return 1
            
            res = 0
            for i in range(n):
                if i not in used_cols and (curr_row + 1 + i) not in used_diag_1 and (curr_row + 1 - i) not in used_diag_2: 
                    res += dfs(curr_row + 1, i)
            
            used_rows.remove(curr_row)
            used_cols.remove(curr_col)
            used_diag_1.remove(curr_row + curr_col)
            used_diag_2.remove(curr_row - curr_col)
            
            return res
        
        res = 0
        for i in range(n):
            res += dfs(0, i)
        return res