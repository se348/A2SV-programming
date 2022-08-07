"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

from typing import List


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        soln=[]
        for i in range(1,1001):
            a= self.checkX(customfunction, i, z)
            if a!=-1:
                soln.append([a,i])
        return soln
    def checkX(self,customfunction, y, z):
        low=1
        high=1000
        while low<=high:
            mid= (low+high)//2
            soln= customfunction.f(mid,y)
            if soln ==z:
                return mid
            elif soln> z:
                high=mid-1
            else:
                low= mid+1
        return -1
    
            