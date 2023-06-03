class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[-1 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        queue = deque()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    queue.append((i,j, 0))
                    result[i][j] = 0
                    
        inbound = lambda x,y : 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and result[x][y] == -1
        
        while queue:
            prev_x,prev_y,d = queue.popleft()
            
            for i, j in directions:
                if inbound(prev_x + i, prev_y + j):
                    
                    result[prev_x + i][prev_y + j] = d + 1
                    queue.append((prev_x + i,prev_y + j, d+ 1))
                    
        return result