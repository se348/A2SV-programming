class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
        
        def find(child):
            if parent[child] == child:
                return child
            
            parent[child] =  find(parent[child])
            return parent[child]
        
        def union(c1, c2):
            p1 , p2 = find(c1), find(c2)
            
            if p1 == p2:
                return
            
            if rank[p1] > rank[p2]:
                parent[p2] = parent[p1]
                rank[p1] += rank[p2]
                
            else:
                parent[p1] = parent[p2]
                rank[p2] += rank[p1]

        
        for a1, a2 in edges:
            n1 = a1 - 1
            n2 = a2 - 1
            
            prev1 = find(n1)
            prev2 = find(n2)
            
            union(n1, n2)
            
            curr1 = find(n1)
            curr2 = find(n2)
            
            if prev1 == curr1 and prev2 == curr2:
                return [a1, a2]
        