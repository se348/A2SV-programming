class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        past1 = edges[0][0]
        past2 = edges[0][1]
        
        if edges[1][0] == past1 or edges[1][0]== past2:
            return edges[1][0]
        
        if edges[1][1] == past1 or edges[1][1]== past2:
            return edges[1][1]