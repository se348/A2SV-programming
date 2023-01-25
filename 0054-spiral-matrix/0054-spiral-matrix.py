class Solution:
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        curr_dx, curr_dy = 0, 1 # to the right
        curr_row, curr_col = 0, 0
        ans = []
        n, m = len(matrix), len(matrix[0])
        seen = set()
        inbound = lambda x, y : 0 <= x < n and 0 <= y < m
        
        while len(ans) < n * m:
            if (curr_row, curr_col) not in seen:
                ans.append(matrix[curr_row][curr_col])
            seen.add((curr_row, curr_col))
            
            if not inbound(curr_row + curr_dx, curr_col + curr_dy) or\
                (curr_row + curr_dx, curr_col + curr_dy) in seen:
                curr_dx, curr_dy = curr_dy, -1 * curr_dx
            else:
                curr_row, curr_col = curr_row + curr_dx, curr_col + curr_dy
        return ans
            
        
        
        
        
        
        
        
        
        
        
        
        
        # direct =[1, 0]
        # curr =[0,0]
        
#         res = []
        
#         while True:
#             new_curr = curr + direct
#             new_dirr = [curr + direct[1], curr + (-1 * direct[0])]
            
            
#             if (new_curr[0] < len(matrix) and new_curr[1] < len(matrix[0])) and matrix[new_curr[0]][new_curr[1]] != -101:
#                 curr = new_curr
#                 continue
                
#             elif new_dirr[0] < len(matrix) and new_dirr[1] < len(matrix[0]) and matrix[new_dirr[0]][new_dirr[1]] != -101:
#                 curr = new_dirr
#                 direct = []
                
#             else:
#                 break
                
                