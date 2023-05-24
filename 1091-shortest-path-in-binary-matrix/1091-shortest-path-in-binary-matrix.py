class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directionMat =[
                            [0,1], [0,-1], [1,0], [-1, 0],
                            [-1, 1], [1, -1], [-1, -1], [1,1]
                      ]
        
        source = [0, 0]
        inbound = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]==0
        queue= deque([source])
        if grid[0][0] == 1:
            return -1
        grid[0][0] = 1
        count = 1
        
        while queue:
            for i in range(len(queue)):
                curr_x, curr_y = queue.popleft()
                if curr_x == len(grid) -1 and curr_y == len(grid[0]) - 1:
                    return count
                
                for n_x, n_y in directionMat:
                    x= curr_x + n_x
                    y = curr_y + n_y
                    
                    if inbound(x, y):
                        grid[x][y] = 1
                        queue.append((x, y))
            count += 1
            
        return -1