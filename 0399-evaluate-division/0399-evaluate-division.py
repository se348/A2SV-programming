class Solution:
    def dfs(self, currElem, target, visited, graph):
        visited.add(currElem)
        if currElem == target and target in graph:
            return 1
        
        for neighbor, weight in graph[currElem]:
            
            if neighbor not in visited:
                curr = self.dfs(neighbor, target, visited, graph)
                if curr:
                    return curr * weight
        
        return 0
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        
        for i, equation in enumerate(equations):
 
            graph[equation[0]].append((equation[1], values[i]))
            graph[equation[1]].append((equation[0], 1 / values[i]))
        
        res = []
        for source, target in queries:
            visited = set()
            temp = self.dfs(source, target, visited, graph)
            res.append(temp if temp else -1)
            
        return res