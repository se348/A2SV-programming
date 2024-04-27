class UF:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        
    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[px] = py
            self.rank[py] += 1
            
    def same_group(self, x, y):
        return self.find(x) == self.find(y)
    
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        listt = list(range(len(queries)))
        listt.sort(key = lambda x: queries[x][2])
        
        edgeList.sort(key = lambda x: x[2])
        
        uf = UF(n)
        curr = 0
        res = [False] * len(queries)
        
        for ind in range(len(listt)):
            value = queries[listt[ind]]
            
            while curr < len(edgeList):
                if edgeList[curr][2] >= value[2]:
                    break
                
                uf.union(edgeList[curr][0], edgeList[curr][1])
                curr += 1
            
            res[listt[ind]] = uf.same_group(value[0], value[1])
        
        return res