class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        visited= set()
        min_heap = [(0,0,0)]
        n, m = len(heights), len(heights[0])
        inbound = lambda x,y: 0<= x < n and 0<= y < m and (x,y) not in visited
        directions = [[1,0], [0,1], [-1, 0], [0, -1]]
        
        while min_heap:
            max_dist, curr_x, curr_y = heapq.heappop(min_heap)
            if (curr_x, curr_y) in visited:
                continue
            visited.add((curr_x, curr_y))
            if curr_x == n - 1 and curr_y == m - 1:
                return max_dist
        
            curr_val = heights[curr_x][curr_y]
            for i,j in directions:
                if inbound(i + curr_x, j + curr_y):
                    next_val = heights[i + curr_x][j + curr_y]
                    temp = abs(next_val - curr_val)
                    temp = max(temp, max_dist)
                    heapq.heappush(min_heap, (temp, i + curr_x, j + curr_y ))
                    