class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        pathDiction =[-1] * len(graph)
        
        def dfs(i, value):
            pathDiction[i] = value
            
            for neighbor in graph[i]:
                if pathDiction[neighbor] == -1:
                    if not dfs(neighbor, 1 - value):
                        return False
                elif pathDiction[neighbor] == pathDiction[i]:
                    return False
            return True
        
        for i in range(len(graph)):
            if pathDiction[i] == -1:
                if not dfs(i, 0):
                    return False
        return True