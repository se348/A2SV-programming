class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        adjacencyList = collections.defaultdict(list)
        visited = set()
        
        def dfs(curr):
            
            for i in adjacencyList[curr]:
                if i not in visited:
                    visited.add(i)
                    dfs(i)
                    
        for i in range(len(isConnected)):
            for j in range(i):
                
                if isConnected[i][j] == 1:
                    adjacencyList[i].append(j)
                    adjacencyList[j].append(i)
                    
        visited.add(0)
        dfs(0)
        count = 1
        
        for i in range(1, len(isConnected)):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count
        
            
            
        
        