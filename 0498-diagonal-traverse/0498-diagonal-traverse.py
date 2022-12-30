class Solution:
    def findNumsWithSum(self, total, rows, cols, up):
        
        res= []
        
        if up:
            for j in range(rows-1, -1,-1):
                col = total - j
                if col > cols-1 or col < 0:
                    continue
                res.append([j, col])
                
        else:
            for j in range(rows):
                col = total - j
                if col < 0 or col > cols - 1:
                    continue
                res.append([j, col])
            
        
        return res
        
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        up = True
        count = len(mat) + len(mat[0]) -1
        res = []
        
        for i in range(count):
            to_be_added = self.findNumsWithSum(i, len(mat), len(mat[0]), up)
        
            for j, k in to_be_added:
                res.append(mat[j][k])
            
            up = not up 
        
        return res