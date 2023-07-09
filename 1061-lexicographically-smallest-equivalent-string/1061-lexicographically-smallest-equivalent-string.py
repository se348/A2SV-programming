class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        
        for i in s1:
            parent[i] = i
        for i in s2:
            parent[i] = i
        
        rank = defaultdict(lambda: 1)
        
        def find(child1):
            if child1 == parent[child1]:
                return child1
            
            parent[child1] = find(parent[child1])
            return parent[child1]
        
        def union(ch1, ch2):
            par1 = find(ch1)
            par2 = find(ch2)
            
            if par1 == par2:
                return 
            
            if rank[par1] > rank[par2]:
                parent[par2] = parent[par1]
                rank[par1] += rank[par2]
                
            else:
                parent[par1] = parent[par2]
                rank[par2] += rank[par1]
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
            
            
        sameRep = defaultdict(list)
        
        for ch, par in parent.items():
            sameRep[find(par)].append(ch)
            
        for i in sameRep:
            sameRep[i].sort()
            
        result = []
        for char in baseStr:
            if char in parent:
                par = find(char)
                result.append(sameRep[par][0])
            else:
                result.append(char)
        return "".join(result)
                