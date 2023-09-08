class UnionFind:
    def __init__(self, parent):
        self.parent = parent
        self.rank = defaultdict(int)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_parent = defaultdict(list)
        col_parent = defaultdict(list)
        diction = {}
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_parent[i].append((i, j))
                    col_parent[j].append((i, j))
                    diction[(i, j)] = (i, j)
                    
        s = UnionFind(diction)
        
        for key in row_parent:
            for i in range(len(row_parent[key]) - 1):
                s.union(row_parent[key][i], row_parent[key][i + 1])
        
        for key in col_parent:
            for i in range(len(col_parent[key]) - 1):
                s.union(col_parent[key][i], col_parent[key][i + 1])
        
        counts = defaultdict(int)
        for key in s.parent:
            counts[s.find(key)] += 1
        alones = 0
        for key in counts:
            num = counts[key]
            if num == 1:
                alones += 1
        
        return len(s.parent) - alones
        