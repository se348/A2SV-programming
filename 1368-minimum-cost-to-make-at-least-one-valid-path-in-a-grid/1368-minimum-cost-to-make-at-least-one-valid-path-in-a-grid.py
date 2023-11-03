class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n, m= len(grid), len(grid[0])
        
        directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        min_heap =  [(0, 0, 0)]
        
        dirs = [1, 2, 3, 4 ]
        
        inbound = lambda x, y: 0  <= x < n and 0 <= y < m
        
        costs = [[inf for _ in range(m)]for _ in range(n)]
        
        costs[0][0] = 0
        
        while min_heap:
            curr_cost, x, y = heapq.heappop(min_heap)
            
            if x == (n - 1) and y == (m - 1):
                return curr_cost
            
            if curr_cost > costs[x][y]:
                continue
            
            for nxt in dirs:
                
                nxt_x, nxt_y = directions[nxt]
                nxt_x += x
                nxt_y += y
                
                if not inbound(nxt_x, nxt_y):
                    continue
                
                if nxt == grid[x][y]:
                    if curr_cost < costs[nxt_x][nxt_y] :
                        costs[nxt_x][nxt_y] =  curr_cost
                        heapq.heappush(min_heap, (curr_cost, nxt_x, nxt_y))
                else:
                    if (curr_cost + 1) < costs[nxt_x][nxt_y]:
                        costs[nxt_x][nxt_y] =  curr_cost + 1
                        heapq.heappush(min_heap, (curr_cost + 1, nxt_x, nxt_y))
                        
                    