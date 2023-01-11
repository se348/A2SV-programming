class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        visited = set()
        
        def dfs(curr_index):
            visited.add(curr_index)
            foundApple, quantity = False, 0 
            
            for vertice in graph[curr_index]:
                if vertice not in visited:
                    curr_found, curr_quantity =dfs(vertice)
                    foundApple = foundApple or curr_found
                    quantity += curr_quantity
                    if curr_found:
                        quantity += 2

            if hasApple[curr_index]:
                foundApple = True
                
            return foundApple, quantity
        
        for vert1, vert2 in edges:
            
            graph[vert1].append(vert2)
            graph[vert2].append(vert1)
            
        return dfs(0)[1]
        
        