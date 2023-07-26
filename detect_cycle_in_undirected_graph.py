def isCycle(V: int, adj: List[List[int]]) -> bool:
    visit_track = [-1 for i in range(V)]
    
    def dfs(ind, parent):
        for neighbor in adj[ind]:
            if visit_track[neighbor] == -1:
                visit_track[neighbor] = 1
                if dfs(neighbor, ind):
                    return True
            elif parent and neighbor != parent and visit_track[neighbor] == 1:
                return True
            
        
        return False
    
    
    for i in range(V):
        if visit_track[i] == 1:
            continue
        visit_track[i] = 1
        parent = None
        if dfs(i, parent):
            return True
    return False
