class Solution:
    def constructGraph(self, bombs):
        damage_list = [[] for i in range(len(bombs))]
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                x_diff = bombs[j][1] - bombs[i][1]
                y_diff = bombs[j][0] - bombs[i][0]
                
                hypoth = ((x_diff ** 2) + (y_diff ** 2)) ** 0.5
                
                if hypoth <= bombs[i][2]:
                    damage_list[i].append(j)
                
                if hypoth <= bombs[j][2]:
                    damage_list[j].append(i)
        return damage_list
                
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adjacency_list = self.constructGraph(bombs)
        visited = set()
        
        def dfs(ind):
            visited.add(ind)
            
            for i in adjacency_list[ind]:
                if i not in visited:
                    dfs(i)
        
        count = 0
        for i in range(len(bombs)):
            visited = set()
            dfs(i)
            count =max(count, len(visited))
            
        return count
