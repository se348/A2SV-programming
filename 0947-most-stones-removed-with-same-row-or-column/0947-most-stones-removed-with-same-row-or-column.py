class Solution:
    
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
        def find(char):
            p = parent[char]
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
        
        for i in range(n):
            row, col = stones[i]
            
            rows[row].append(i)
            cols[col].append(i)
            
        for i in rows.values():
            for j in range(len(i) -1):
                union(i[j], i[j + 1])
        
        for i in cols.values():
            for j in range(len(i) - 1):
                union(i[j], i[j + 1])
        
        uniques = set()
        for i in parent:
            uniques.add(find(i))
            
        return n - len(uniques)
        
        