class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target:
            return 0
        
        adjacencyList = defaultdict(set)
        
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                adjacencyList[routes[i][j]].add(i)
                
        queue = deque()
        visited = set()
        
        for ind in adjacencyList[source]:
            queue.append((ind, 1))
            visited.add(ind)
            
        while queue:
            ind, count = queue.popleft()
            
            if target in routes[ind]:
                return count
            
            for node in routes[ind]:
                for next_ind in adjacencyList[node]:
                    if next_ind not in visited:
                        visited.add(next_ind)
                        queue.append((next_ind, count + 1))
        
        return -1