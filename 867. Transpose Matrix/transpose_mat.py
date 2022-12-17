from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        for i,val in enumerate(matrix):
            for j in range(len(matrix[0])):
                res[j][i] =matrix[i][j]
        return res