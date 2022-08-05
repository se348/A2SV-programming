from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        start= 0
        end= len(grid[0])-1
        count =0 
        for i in range(len(grid)-1, -1,-1):
            start = self.findNegativesInRow(grid[i], start, end)
            if (start==-1): break
            count+= (end-start)+1
            print(start, grid[i],count)

        return count

    def findNegativesInRow(self, row, start, end):
        while start<=end:
            mid= (start + end)//2
            print(start, mid,end)
            if row[start]<0:
                return start
            elif mid> start and row[mid]<0 and row[mid-1]>=0:
                return mid
            elif row[mid] <0:
                end= mid-1
            else: start =mid+1
        return -1    

