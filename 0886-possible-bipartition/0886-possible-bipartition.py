class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjacencyList= [[] for i in range(n)]
        pathDiction =[-1] * n
        
        def dfs(i, value):
            pathDiction[i] = value
            
            for neighbor in adjacencyList[i]:
                if pathDiction[neighbor] == -1:
                    if not dfs(neighbor, 1 - value):
                        return False
                elif pathDiction[neighbor] == pathDiction[i]:
                    return False
            return True
        
        for i, j in dislikes:
            adjacencyList[i -1].append(j - 1)
            adjacencyList[j -1].append(i - 1)
            
        for i in range(n):
            if pathDiction[i] == -1:
                if not dfs(i, 0):
                    return False
        return True
        