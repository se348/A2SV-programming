class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def dfs(curr, visited):
            visited.add(curr)
            
            for neighbor in rooms[curr]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
        
        visited = set()
        dfs(0, visited)
        
        if len(visited) == len(rooms):
            return True
        
        return False