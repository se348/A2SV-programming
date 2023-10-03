class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        current_find = defaultdict(lambda: inf)
        
        
        directions= [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        isValid = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited
        
        while heap:
            
            value, x, y = heapq.heappop(heap)
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return value
            
            visited.add((x, y))
            
            for neighbor in directions:                
                if isValid(x + neighbor[0], y + neighbor[1]):
                    next_val = max(grid[x + neighbor[0]][y + neighbor[1]], value) 
                    
                    if next_val < current_find[(x + neighbor[0], y + neighbor[1])]:
                        current_find[(x + neighbor[0], y + neighbor[1])] =  next_val
                        heapq.heappush(heap, (next_val, x + neighbor[0], y + neighbor[1]))
            