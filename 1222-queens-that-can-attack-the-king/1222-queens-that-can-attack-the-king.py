class Solution:
    
    def findQueen(self, queens_set, king, direction):
        
        curr = king.copy()
        
        while True:
            if curr[0]  < 8 and curr[0]>=0 and curr[1] < 8 and curr[1] >=0:
                
                if tuple(curr) in queens_set:
                    return curr
                
                curr[0] += direction[0]
                curr[1] += direction[1]
            else:
                break    
                
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queen_set = set()
        for queen in queens:
            queen_set.add(tuple(queen))
        
        directions=[[0,1],[1,0],[1,1],[-1,0],[0,-1],[-1,-1],[1,-1],[-1,1]]
        
        result =[]
        for direction in directions:
            curr = self.findQueen(queen_set, king, direction)
            if curr:
                result.append(curr)
        return result