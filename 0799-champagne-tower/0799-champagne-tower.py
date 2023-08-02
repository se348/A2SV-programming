class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glass_list = [[0 for _ in range(query_row + 2)]  for _ in range(query_row + 2)]
        glass_list[0][0]= poured    
        
        for i in range(query_row + 1):
            for j in range(query_glass + 1):
                
                if glass_list[i][j] > 1:
                    diff = glass_list[i][j] - 1
                    glass_list[i + 1][j] += (diff/ 2)
                    glass_list[i + 1][j + 1] += (diff/ 2)
                    
        return min(glass_list[query_row][query_glass], 1)