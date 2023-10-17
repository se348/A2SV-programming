class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = defaultdict(lambda: 1)
        
        for i in range(n):
            for j in range(n):
                self.parent[(i,j)] = (i,j)
    
    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        par1, par2 = self.find(node1), self.find(node2)
        if par1 == par2:
            return
        rank1, rank2 = self.rank[node1], self.rank[node2]
        
        if rank1 >= rank2:
            self.parent[par2] = par1
            self.rank[par1] += self.rank[par2]
        else:
            self.parent[par1] = par2
            self.rank[par2] += self.rank[par1]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        length = len(grid)
        
        inbound = lambda x,y : 0 <= x  < length and 0 <= y < length
        
        uF = UnionFind(length)
        
        for i in range(length):
            for j in range(length):
                
                current = grid[i][j]
                if not current:
                    continue
                    
                if inbound(i + 1, j) and grid[i + 1][j]:
                    uF.union((i,j), (i + 1, j))
                
                if inbound(i, j + 1) and grid[i][j + 1]:
                    uF.union((i,j), (i, j + 1))
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        
        maxim = uF.rank[uF.find((0,0))]
        
        for i in range(length):
            for j in range(length):
                
                if grid[i][j]:
                    continue
                
                
                roots = set()
                temp = 0
                
                for k in range(4):
                    
                    new_x, new_y =directions[k][0] + i, directions[k][1] + j
                    
                    if not inbound(new_x,new_y) or not grid[new_x][new_y]:
                        continue
                    
                    new = uF.find((new_x, new_y))

                    if new in roots:
                        # maxim = max(maxim, uF.rank[new] + 1)
                        continue

                    temp += uF.rank[new]
                    maxim = max(maxim, temp + 1)
                    roots.add(new)
                        
        return maxim 
                    
                
        