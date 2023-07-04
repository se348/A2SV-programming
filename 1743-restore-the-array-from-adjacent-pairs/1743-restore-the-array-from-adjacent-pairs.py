class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        count = defaultdict(int)
        adjacencyList = defaultdict(list)
        
        for i,j in adjacentPairs:
            
            adjacencyList[i].append(j)
            adjacencyList[j].append(i)
            
            count[i] += 1
            count[j] += 1

        res= []
        
        curr = None
        for i, j in count.items():
            if j == 1:
                curr = i
                break
        visited = set()
        
        def dfs(ind):
            res.append(ind)
            visited.add(ind)   
            
            for neighbor in adjacencyList[ind]:
                count[neighbor] -= 1
                if (count[neighbor] == 0 or count[neighbor] == 1) and neighbor not in visited:
                    dfs(neighbor)
        
        count[curr] -= 1
        dfs(curr)            
        return res
                
        