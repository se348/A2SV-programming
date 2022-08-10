from typing import List


class Solution:
    one_set= set()
    traversed =0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def possiblemovements(x,y):
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

        def dfs(x,y):
            self.traversed+=1
            self.one_set.remove((x,y))
            for i,j in possiblemovements(x,y):
                if grid[i][j]==1 and (i,j) in self.one_set:
                       dfs(i,j)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==1:
                   self.one_set.add((i,j))
        ans=0
        while self.one_set:
            llist = list(self.one_set)
            ans= max(self.traversed, ans)
            self.traversed=0
            dfs(llist[0][0],llist[0][1]) 
        ans= max(self.traversed, ans)
        return ans
s= Solution()
grid = [[1]]
a = s.maxAreaOfIsland(grid)
print(a)        
            