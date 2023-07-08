class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        n = len(s)
        parent = [i for i in range(n)]
        rank = [ 1 for i in range(n)]
        
        def find(child):
            if child == parent[child]:
                return child
            parent[child] = find(parent[child])
            return parent[child]
        
        def union(child1, child2):
            par1 = find(child1)
            par2 = find(child2)
            
            if par1 == par2:
                return 
            
            if rank[par1] > rank[par2]:
                parent[par2] = parent[par1]
                rank[par1] += rank[par2]
                
            else:
                parent[par1] = parent[par2]
                rank[par2] += rank[par1]
                
        for node1, node2 in pairs:
            union(node1, node2)
            
        connected = defaultdict(list)
        
        for i in range(n):
            connected[find(parent[i])].append(i)
         
        result = [ch for ch in s]
        
        for cons in connected.values():
            chars = []
            
            for ind in cons:
                chars.append(s[ind])
            chars.sort()
            
            count = 0
            for ind in cons:
                result[ind] =chars[count]
                count += 1
                
        return "".join(result)
            
            
        
        