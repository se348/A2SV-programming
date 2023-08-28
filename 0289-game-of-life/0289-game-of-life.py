class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                board[i][j] += 1
        
        directions = [[1,0], [0, 1],[-1, 0], [0, -1], [1, -1], [-1, 1], [1, 1], [-1, -1]]
        inbound = lambda x, y: 0<= x <n and 0 <= y < m

        for i in range(n):
            for j in range(m):
                alive = 0

                for dir_x, dir_y in directions:
                    next_x, next_y = dir_x + i , dir_y + j
                    
                    if not inbound(next_x, next_y):
                        continue
                    
                    if board[next_x][next_y] == 2:
                        alive +=1
                    elif board[next_x][next_y] == -2:
                        alive +=1
                if board[i][j] == 2:
                    if alive < 2 or alive > 3:
                        board[i][j] = -2
                else:
                    if alive == 3:
                        board[i][j] = -1


        for i in range(n):
            for j in range(m):
                if board[i][j] == 2 or board[i][j] == -1:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        
