class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        
        mat = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1,-1, -1):
                
                if i == n - 1 and j== m - 1:
                    mat[i][j] = min(dungeon[i][j], 0)
                elif i == n - 1:
                    mat[i][j] = min(dungeon[i][j] + mat[i][j + 1] , 0)
                elif j == m - 1:
                    mat[i][j] = min(dungeon[i][j] + mat[i + 1][j] , 0)
                else:
                    temp = max(mat[i][j + 1], mat[i + 1][j])
                    mat[i][j] = min(temp + dungeon[i][j], 0)
        res = max(0, 0 - mat[0][0]) + 1
        return res
                    