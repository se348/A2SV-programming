class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        direction = [[1,0], [0, 1], [-1, 0], [0, -1]]
        inbound = lambda x, y : 0 <= x < len(image) and 0 <= y < len(image[0])
        visited = {(sr, sc)}
        
        
        def dfs(curr_x, curr_y):
            
            for i, j in direction:
                new_x = i + curr_x
                new_y = j + curr_y
                
                if inbound(new_x, new_y) and image[new_x][new_y] == origin_col and (new_x, new_y) not in visited:
                    image[new_x][new_y] = color
                    visited.add((new_x, new_y))
                    dfs(new_x, new_y)
                
        
        origin_col = image[sr][sc]
        if origin_col == color:
            return image
        
        image[sr][sc] = color
        dfs(sr, sc)
        
        return image
        