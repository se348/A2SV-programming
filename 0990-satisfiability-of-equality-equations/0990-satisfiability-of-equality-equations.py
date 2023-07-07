class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        unequals = []
        parent = defaultdict(str)
        rank = defaultdict(int)
        for eq in equations:
            parent[eq[0]] = eq[0]
            parent[eq[3]] = eq[3]

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
        
        for eq in equations:
            if eq[1] == '!':
                unequals.append((eq[0], eq[3]))
            else:
                union(eq[0], eq[3])
        
        for c1, c2 in unequals:
            if find(c1) == find(c2): return False
        
        return True