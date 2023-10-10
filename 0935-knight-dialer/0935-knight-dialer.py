class Solution:
    def knightDialer(self, n: int) -> int:
        
        
        
        
        moves = [[] for i in range(10)]
        
        directions = [[1, 2], [2,  1], [-1, 2], [-2, 1], [-1, -2], [-2, -1], [1, -2], [2, -1]]
        
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
        
        inbound = lambda x, y: 0 <= x < 4 and 0 <= y< 3 and mat[x][y] != -1
        
        
        @cache
        def dp(number,  remaining):
            
            if remaining == 1:
                return 1
            
            count = 0
            
            for neighbor in moves[number]:
                if neighbor != -1:
                    count += dp(neighbor, remaining - 1)
            
            mod = (10 ** 9) + 7
            return (count % mod)
        
        for i in range(4):
            for j in range(3):
                if not inbound(i,j):
                    continue
                for dir_i, dir_j in directions:
                    if inbound(dir_i + i, dir_j + j):
                        current_number = mat[i][j]
                        moves[current_number].append(mat[dir_i + i][ dir_j + j])
        
        count = 0
        mod = (10 ** 9) + 7
        for i in range(10):
            count += dp(i, n)  
        return (count % mod)
                        
                
            
                        
                
        