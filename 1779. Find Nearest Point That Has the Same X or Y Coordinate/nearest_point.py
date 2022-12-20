class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        res_val=math.inf
        res_ind= -1
        
        for ind, [i,j] in enumerate(points):
            if i!=x and j!=y:
                continue
                
            val = abs(i-x) + abs(j-y)
            if val< res_val:
                res_val = val
                res_ind = ind
        
        return res_ind
            