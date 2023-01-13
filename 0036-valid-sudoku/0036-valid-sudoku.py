class Solution:
    def squareValidity(self, board, curr_row, curr_col):
        check = set()
        for row in range(curr_row, curr_row + 3):
            for col in range(curr_col, curr_col +3):
                if board[row][col] == ".":
                    continue
                if board[row][col] in check:
                    return False
                check.add(board[row][col])
                
        return True
                    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(0,len(board),3):
            for col in range(0, len(board[0]),3):
                temp= self.squareValidity(board, row, col)
                
                if not temp:
                    return False
                
        col_list = [set() for j in range(len(board[0]))]
        row_list = [set() for i in range(len(board))]
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                
                if val == ".":
                    continue
                    
                if val in col_list[col] or val in row_list[row]:
                    return False
                
                col_list[col].add(val)
                row_list[row].add(val)
                
        return True