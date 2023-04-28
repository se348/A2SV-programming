class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        length = 9
        
        rows_tracker = [set() for i in range(length)]
        cols_tracker = [set() for i in range(length)]
        box_tracker =  [[set() for i in range(3)] for j in range(3)]
        path = []

        def dfs(l):
            if l == len(path):  
                return True
            
            i = path[l][0]
            j = path[l][1]
            
            for k in range(1, length + 1):
                
                if str(k) in rows_tracker[i]:
                    continue
                if str(k) in cols_tracker[j]:
                    continue
                if str(k) in box_tracker[i // 3][j // 3]:
                    continue
                
                board[i][j] = str(k)
                
                rows_tracker[i].add(str(k))
                cols_tracker[j].add(str(k))
                box_tracker[i // 3][j // 3].add(str(k))
                
                cond = dfs(l + 1)
                if not cond:
                    board[i][j] = "."
                    
                    rows_tracker[i].remove(str(k))
                    cols_tracker[j].remove(str(k))
                    box_tracker[i // 3][j // 3].remove(str(k))
                else:
                    return True
            return False
        
        for i in range(length):
            for j in range(length):
                if board[i][j] != ".":
                    rows_tracker[i].add(board[i][j])
                    cols_tracker[j].add(board[i][j])
                    box_tracker[i // 3][j // 3].add(board[i][j])
                else:
                    path.append((i, j))
        dfs(0)