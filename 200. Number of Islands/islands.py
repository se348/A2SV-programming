from typing import List


class Solution:
    one_set= set()
    def numIslands(self, grid: List[List[str]]) -> int:
        def findNeighbors(x,y):
            ans=[]
            if y< (len(grid[0])-1):
                ans.append([x, y+1])
            if x>0:
                ans.append([x-1,y])
            if x<(len(grid)-1):
                ans.append([x+1, y])
            if y>0:
                ans.append([x,y-1])
            return ans
        def dfs(x,y):
            self.one_set.remove((x,y))
            for (i,j) in findNeighbors(x,y):
                if grid[i][j]=="1" and((i,j)) in self.one_set:
                    dfs(i,j)
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.one_set.add((i,j))
        count=0
        while self.one_set:
            count+=1
            llist= list(self.one_set)
            dfs(llist[0][0],llist[0][1])
        return count