class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
        roads.sort(key=lambda x: x[2])

        def find(city):
            p = parent[city]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(c1, c2):
            p1, p2 = find(c1), find(c2)
            if p1 == p2: return
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
        
        for a, b, distance in roads:
            union(a, b)
        
        for a, b, distance in roads:
            if find(1) == find(a): return distance