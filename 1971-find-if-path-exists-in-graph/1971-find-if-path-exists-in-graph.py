class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
        def find(node):
            if parent[node] == node:
                return node
            
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            
            if parent1 == parent2:
                return
            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
                
        for node1,node2 in edges:
            union(node1, node2)
        
        if find(source) == find(destination):
            return True
        return False