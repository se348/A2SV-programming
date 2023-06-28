class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row = 0
        max_count = 0
        
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[0])):
                if mat[i][j]:
                    count += 1
            if count > max_count:
                row = i
                max_count = count
        
        return [row, max_count]
        