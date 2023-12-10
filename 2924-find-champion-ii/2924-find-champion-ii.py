class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        incoming = n
        
        for i, j in edges:
            
            indegree[j] += 1
            
            if indegree[j] ==  1:
                incoming -= 1
        
        if incoming != 1:
            return -1
        
        for i in range(n):
            if indegree[i] == 0:
                return i