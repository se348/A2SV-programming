class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        firstarr= matrix[0][:-1]
        
        for row in range(1, len(matrix)):
            curr = matrix[row][1:]
            print(firstarr,curr)
            if firstarr == curr:
                firstarr = matrix[row][:-1]
                continue
            else:
                return False
        
        return True
            