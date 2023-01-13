class Solution:
    def matrixReshape(self, matrix: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if len(matrix) * len(matrix[0]) != r * c:
            return matrix
        
        new_mat = [[0 for column in range(c)] for row in range(r) ]
        count = 0
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                
                curr_col = count % c
                curr_row = count // c
                new_mat[curr_row][curr_col] = matrix[row][col]
                count += 1
                
        return new_mat