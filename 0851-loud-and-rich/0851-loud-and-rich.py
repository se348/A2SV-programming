class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adjacencyList = defaultdict(list)
        visited = set()
        def dfs(i):
            
            visited.add(i)
            temp = math.inf
            for neighbor in adjacencyList[i]:
                if neighbor not in visited:
                    temp = min(temp, dfs(neighbor))
                    temp = min(quiet[neighbor], temp)
            
            temp = min(quiet[i], temp)
            return temp
        
        for a,b in richer:
            adjacencyList[b].append(a)
        
        n = len(quiet)  
        quiet_diction =  {}
        
        for i in range(n):
            quiet_diction[quiet[i]] = i
            
        result = []
        
        for i in range(n):
            visited = set()
            result.append(quiet_diction[dfs(i)])
        
        return result
        