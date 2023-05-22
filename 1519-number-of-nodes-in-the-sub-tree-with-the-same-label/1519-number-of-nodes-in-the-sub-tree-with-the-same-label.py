class Solution:
    def dfs(self, ind, adjacencyList, labels, arr, visited):
        visited.add(ind)
        if len(adjacencyList[ind]) == 0:
            leaf =[0] * 26
            leaf[ord(labels[ind]) - ord('a')] += 1
            arr[ind] = leaf[ord(labels[ind]) - ord('a')]
            return leaf
        
        res = [0] * 26
        for neighbor in adjacencyList[ind]:
            if neighbor not in visited:
                chars= self.dfs(neighbor, adjacencyList, labels, arr, visited)
                for i in range(26):
                    res[i] += chars[i]
        
        res[ord(labels[ind]) - ord('a')] +=1
        arr[ind] = res[ord(labels[ind]) - ord('a')]
        return res    
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = defaultdict(list)
        
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        arr= [0] *n
        visited = set()
        self.dfs(0, adj, labels, arr, visited)
        return arr