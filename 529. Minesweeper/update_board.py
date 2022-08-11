from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        def findNeighbors(x,y):
            ans=[]
            if y< (len(board[0])-1):
                ans.append([x, y+1])
            if x>0:
                ans.append([x-1,y])
            if x<(len(board)-1):
                ans.append([x+1, y])
            if y>0:
                ans.append([x,y-1])
            if y< (len(board[0])-1) and x<(len(board)-1):
                ans.append([x+1, y+1])
            if x>0 and y>0:
                ans.append([x-1,y-1])
            if x<(len(board)-1) and y>0:
                ans.append([x+1, y-1])
            if x>0 and  y< (len(board[0])-1):
                ans.append([x-1,y+1])       
            return ans
        def dfs(x,y):
            if board[x][y] == "E":  
                neighbors =findNeighbors(x,y)
                hasAdjacementMine = 0
                for (i,j) in neighbors:
                    if board[i][j] =="M" or board[i][j] =="X":
                        hasAdjacementMine+=1
                if hasAdjacementMine!=0:
                    board[x][y]= str(hasAdjacementMine)
                else:
                    board[x][y]="B"
                    for (i,j) in neighbors:
                        dfs(i,j)
            elif board[x][y] == "M":
                board[x][y]="X"

        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]]= "X"
        if board[click[0]][click[1]]== "E":
            dfs(click[0],click[1])
        return board
board= [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]
s= Solution()
s.updateBoard(board, click)
print(board)