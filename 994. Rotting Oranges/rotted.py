# work around the code
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def find_neighbor(x,y):
            res = []
            if x>=1 and grid[x-1][y]==1:
                res.append((x-1,y))
            if y>=1 and grid[x][y-1]==1:
                res.append((x,y-1))
            if x< (len(grid) -1) and grid[x+1][y]==1:
                res.append((x+1, y))
            if y< (len(grid[0]) -1) and grid[x][y+1]==1:
                res.append((x,y+1))
            return res
        
        
        initial_twos= deque([])
        initial_ones =set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==1:
                    initial_ones.add((i,j))
                if grid[i][j] ==2:
                    initial_twos.append((i,j))
        q= deque()
        minutes= 0
        for  i in initial_twos:
            q.append((i,0))
        while q:
            val, check= q.popleft()
            for i,j in find_neighbor(val[0], val[1]):
                if (i,j) in initial_ones:
                    initial_ones.remove((i,j))
                grid[i][j] =2
                q.append(((i,j), check+1))
            minutes= check
        if len(initial_ones)==0:
            return minutes
        else:
            return -1