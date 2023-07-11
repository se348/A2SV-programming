class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inward = [0 for i in range(n)]
        
        for i,j in edges:
            inward[j] += 1
            
        result = []
        for i in range(n):
            if inward[i] == 0:
                result.append(i)
                
        return result