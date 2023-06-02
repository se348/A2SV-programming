class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        queue = deque()
        visited_pacific = set()
        directions = [[1,0], [0,1], [-1, 0], [0, -1]]
        inbound_pacific = lambda x, y: 0<= x< len(heights) and 0 <= y <len(heights[0]) and (x,y) not in visited_pacific
        
        for i in range(len(heights)):
            queue.append((i,0))
            visited_pacific.add((i,0))
            
        for i in range(1, len(heights[0])):
            queue.append((0, i))
            visited_pacific.add((0, i))
        
        while queue:
            prev_x, prev_y = queue.popleft()
            
            for i, j in directions:
                if inbound_pacific(prev_x +i, prev_y + j) and heights[prev_x][prev_y] <= heights[prev_x + i][prev_y + j]:
                    queue.append((prev_x +i, prev_y + j))
                    visited_pacific.add((prev_x +i, prev_y + j))

        visited_atlantic = set()
        inbound_atlantic = lambda x, y: 0<= x< len(heights) and 0 <= y <len(heights[0]) and (x,y) not in visited_atlantic
        
        for i in range(len(heights)):
            queue.append((i,len(heights[0]) -1))
            visited_atlantic.add((i,len(heights[0]) -1))
        
        for i in range(0, len(heights[0]) - 1):
            queue.append((len(heights) -1, i))
            visited_atlantic.add((len(heights) -1, i))
            
        while queue:
            prev_x, prev_y = queue.popleft()
            for i, j in directions:
                if inbound_atlantic(prev_x +i, prev_y + j) and heights[prev_x][prev_y] <= heights[prev_x + i][prev_y + j]:
                    queue.append((prev_x +i, prev_y + j))
                    visited_atlantic.add((prev_x +i, prev_y + j))

        return visited_atlantic.intersection(visited_pacific)