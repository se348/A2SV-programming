class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count =  0
        
        queue = deque()
        direction= [(0,1), (0, -1), (-1, 0), (1, 0)]
        visited = set()
        inbound = lambda x, y: 0<= x < len(grid) and 0<= y < len(grid[0]) and (x,y) not in visited and 1 <= grid[x][y] <= 2
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if 1<= grid[i][j] <= 2:
                    count += 1
                if grid[i][j] == 2:
                    queue.append((i,j, 0))
                    visited.add((i,j))
        
        res= 0
        while queue:
            
            curr_x, curr_y, mins = queue.popleft()
            res = mins    
            count -= 1
            
            for dir_x, dir_y in direction:
                neighbor_x = dir_x + curr_x
                neighbor_y = dir_y + curr_y
                
                if inbound(neighbor_x, neighbor_y):
                    visited.add((neighbor_x, neighbor_y))
                    queue.append((neighbor_x, neighbor_y, mins + 1))
                    
        if count == 0:
            return res
        return -1