class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in visited:
                visited.add(source)
                if source == target: return True
                
                for neighbor in graph[source]:
                    curr= dfs(neighbor, target) 
                    if curr:
                        return curr

        for i, j in edges:
            visited = set()
            if i in graph and j in graph and dfs(i, j):
                return i, j
            graph[i].add(j)
            graph[j].add(i)