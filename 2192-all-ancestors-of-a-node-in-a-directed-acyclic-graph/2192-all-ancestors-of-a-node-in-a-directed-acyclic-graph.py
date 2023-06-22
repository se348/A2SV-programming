class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        adjacencyList = defaultdict(list)
        visited = defaultdict(int)
        result =[set() for i in range(n)]
        
        def dfs(curr):
            visited[curr] = 1
            
            for neighbor in adjacencyList[curr]:
                if visited[neighbor] == 0:
                    dfs(neighbor)
                # elif visited[neighbor] == 2:
                for a in result[neighbor]:
                    result[curr].add(a)
                result[curr].add(neighbor)
            visited[curr] = 2
        
        
        for i in range(len(edges)):
            adjacencyList[edges[i][1]].append(edges[i][0])
            
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
        
        ans = []
        for i in range(n):
            ans.append(sorted(result[i]))

        return ans
        