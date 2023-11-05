class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        costs = [[inf for _ in range(m)] for _ in range(n)]
        
        costs[0][0] = grid[0][0]
        min_heap= [(costs[0][0], 0, 0)]
        
        directions= [[1, 0], [0, 1], [-1, 0], [0, -1]]
        inbound = lambda x, y: 0 <= x < n and 0 <= y < m
        
        while min_heap:
            curr_cost, curr_x, curr_y = heapq.heappop(min_heap)
            
            if curr_x == (n - 1) and curr_y == (m - 1):
                return curr_cost
            
            if curr_cost > costs[curr_x][curr_y]:
                continue
            
            for dir_x, dir_y in directions:
                if inbound(dir_x + curr_x, dir_y + curr_y):
                    if grid[dir_x + curr_x][dir_y + curr_y] and curr_cost + 1 < costs[dir_x + curr_x][dir_y + curr_y]:
                        costs[dir_x + curr_x][dir_y + curr_y] = curr_cost + 1
                        heapq.heappush(min_heap, (curr_cost + 1, dir_x + curr_x, dir_y + curr_y))
                    elif not grid[dir_x + curr_x][dir_y + curr_y] and curr_cost < costs[dir_x + curr_x][dir_y + curr_y]:
                        costs[dir_x + curr_x][dir_y + curr_y] = curr_cost
                        heapq.heappush(min_heap, (curr_cost, dir_x + curr_x, dir_y + curr_y))
            
                
        