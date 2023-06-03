class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue = deque()
        directions = [[-1, 0], [0,1], [1,0],[0, -1]]
        result= math.inf
        visited = set()
        inbound = lambda x,y: 0<=x < len(grid) and 0<=y < len(grid[0]) and (x,y) not in visited and grid[x][y] == 1
        
        a= False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i,j, 0))
                    visited.add((i, j))
                    a=True
                    break
            if a:
                break
                    
        while queue:
            x, y, d= queue.popleft()
            
            for i,j in directions:
                if inbound(x + i, y +j):
                    queue.append((x +i, y + j, 0))
                    visited.add((x + i , y + j))
        
        queue = deque(visited)
        new_inbound = lambda x,y: 0<=x < len(grid) and 0<=y < len(grid[0]) and (x,y) not in visited
        while queue:
            a = queue.popleft()
            x =a[0]
            y =a[1]
            d = 0 if len(a)== 2 else a[2]
            for i, j in directions:
                if new_inbound(x + i, y + j):
                    if grid[x +i][y+j] == 1:
                        return d
                    queue.append((x +i, y + j, d + 1))
                    visited.add((x +i, y + j))
                            