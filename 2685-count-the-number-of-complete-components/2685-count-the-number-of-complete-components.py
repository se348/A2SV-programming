class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(curr, visited, adjacency_list, another_set):
            visited.add(curr)
            another_set.add(curr)
            
            for neighbor in adjacency_list[curr]:
                if neighbor not in visited:
                    dfs(neighbor, visited, adjacency_list, another_set)
        
        adjacency_list = defaultdict(list)
        
        for v1, v2 in edges:
            adjacency_list[v1].append(v2)
            adjacency_list[v2].append(v1)
        
        count = 0
        visited = set()
        
        for i in range(n):
            if i not in visited:
                another_set = set()
                dfs(i, visited, adjacency_list, another_set)
                
                option = True
                
                for n in another_set:
                    if len(adjacency_list[n]) != len(another_set) -1:
                        option= False
                        break
                        
                if option:
                    count += 1
        return count