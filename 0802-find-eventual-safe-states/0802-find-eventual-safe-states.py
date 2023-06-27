class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        isSafe = {}
        
        def dfs(i):
            isSafe[i] = False
            for neighbor in graph[i]:
                if neighbor in isSafe and not isSafe[neighbor]:
                    return
                if neighbor not in isSafe:
                    dfs(neighbor)
                    if not isSafe[neighbor]:
                        return
            isSafe[i] = True
            
        res = []
        for i in range(len(graph)):
            if i in isSafe:
                if isSafe[i]:
                    res.append(i)
            else:
                dfs(i)
                if isSafe[i]:
                    res.append(i)
        return res