class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        queue.append((entrance[0], entrance[1], 0))
        maze[entrance[0]][entrance[1]] = "+"
        inbound = lambda x, y: 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == "."
        directions = [[1,0], [0, 1],[-1, 0], [0, -1]]
        
        while queue:
            x, y, d = queue.popleft()
            if (x == 0 or y == 0 or x == len(maze) -1 or y == len(maze[0]) - 1) and [x, y] != entrance:
                return d
            for [i,j] in directions:
                if inbound(x + i, y + j):
                    queue.append((x + i, y + j, d + 1))
                    maze[x + i][y + j] = "+"
        
        return -1
        
            