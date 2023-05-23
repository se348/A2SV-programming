class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacencyList = defaultdict(list)
        for v1, v2 in edges:
            adjacencyList[v1].append(v2)
            adjacencyList[v2].append(v1)
        
        if source == destination:
            return True
        
        queue = deque()
        visited = {source}
        queue.append(source)
        
        while queue:
            currNode = queue.popleft()
            
            for neighbor in adjacencyList[currNode]:
                if neighbor not in visited:
                    if neighbor == destination:
                        return True
                    queue.append(neighbor)
                    visited.add(neighbor)
        return False