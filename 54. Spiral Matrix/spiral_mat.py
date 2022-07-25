from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t =0
        l =0
        r= len(matrix[0])
        b= len(matrix)
        mat =[]
        while l<r and t<b:
            for i in range(l, r):
                mat.append(matrix[t][i])
            t+=1
            for i in range(t, b):
                mat.append(matrix[i][r-1])
            r-=1
            if l==r or t==b:
                break
            for i in range(r-1, l-1, -1):
                mat.append(matrix[b-1][i])
            b-=1
            for i in range(b-1,t-1,-1):
                mat.append(matrix[i][l])
            l+=1
        return mat