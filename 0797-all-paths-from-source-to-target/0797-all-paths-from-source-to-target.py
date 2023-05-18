class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        
        def dfs(curr, path):
            if curr == len(graph) -1:
                res.append(path[:])
                return
            
            for neighbor in graph[curr]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()
                
        dfs(0, [0])
        return res
            
            