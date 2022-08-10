from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        border_set= set()
        solved_set= set()
        
        def neighbor(x,y):
            ans=[]
            if y< (len(board[0])-1):
                ans.append((x, y+1))
            if x>0:
                ans.append([x-1,y])
            if x<(len(board)-1):
                ans.append([x+1, y])
            if y>0:
                ans.append([x,y-1])
            return ans
        def dfs(r:int,c:int):
            if (r,c) in border_set:
                border_set.remove((r,c))
            if board[r][c] =="O":
                solved_set.add((r,c))
            for i,j in neighbor(r,c):
                if board[i][j]=="O" and (i,j) not in solved_set:
                    dfs(i,j)
            
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (board[r][c]=="O" and ((r==0 or r== len(board)-1)  or (c==0 or c==len(board[0])-1))):
                    border_set.add((r,c))
        while border_set:
            llist =list(border_set)
            dfs(llist[0][0],llist[0][1])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=="O" and ((r,c)) not in solved_set:
                    board[r][c]="X"
s= Solution()
board =[["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
s.solve(board)
print(board)