import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def findNeighbors(x,y):
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
        min_heap = [(grid[0][0],0,0)]
        visited ={(0,0)}
        
        while min_heap:
            curr , r, c = heapq.heappop(min_heap)
            if r ==(len(grid)-1) and c== len(grid)-1:
                return curr
            for new_r, new_c in findNeighbors(r,c):
                if (new_r, new_c) not in visited:
                    heapq.heappush(min_heap, (max(curr, grid[new_r][new_c]), new_r, new_c))
                    visited.add((new_r, new_c))