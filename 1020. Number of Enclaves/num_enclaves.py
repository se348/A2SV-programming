from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        border_set= set()
        solved_set= set()
        
        def neighbor(x,y):
            ans=[]
            if y< (len(grid[0])-1):
                ans.append((x, y+1))
            if x>0:
                ans.append((x-1,y))
            if x<(len(grid)-1):
                ans.append((x+1, y))
            if y>0:
                ans.append((x,y-1))
            return ans
        def dfs(r:int,c:int):
            if (r,c) in border_set:
                border_set.remove((r,c))
            if grid[r][c] ==1:
                solved_set.add((r,c))
            for i,j in neighbor(r,c):
                if grid[i][j]==1 and (i,j) not in solved_set:
                    dfs(i,j)
            
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (grid[r][c]==1 and ((r==0 or r== len(grid)-1)  or (c==0 or c==len(grid[0])-1))):
                    border_set.add((r,c))
        while border_set:
            llist =list(border_set)
            dfs(llist[0][0],llist[0][1])
        count =0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1 and ((r,c)) not in solved_set:
                    count+=1
        return count