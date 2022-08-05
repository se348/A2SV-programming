from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.findRow(matrix, target)
        low =0
        high = len(matrix[0])-1
        while low<=high:
            mid= (low+ high)//2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                high =mid-1
            else: low =mid+1
        return False
        
        
    def findRow(self,matrix, target):
        row=-1
        for i in range(len(matrix)):
            if matrix[i][0]<= target:
                row=i
            else:
                break
        return matrix[row]

s= Solution()
a = s.searchMatrix([[1],[2]],1)
print(a)