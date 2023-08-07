class Unionfind:
    
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        
    def find(self, value):
        if self.parent[value] == value:
            return value
        self.parent[value] = self.find(self.parent[value])
        return self.parent[value]
    
    def union(self, value1, value2):
        par1, par2 = self.find(value1), self.find(value2)
        if par1 == par2:
            return
        if self.rank[par1] > self.rank[par2]:
            self.parent[par2] = self.parent[par1]
            self.rank[par1] += self.rank[par2]
        else:
            self.parent[par1] =self.parent[par2]
            self.rank[par2] += self.rank[par1]
        
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        unionfind = Unionfind(n)
        results = []
        
        for i, j in requests:
            cond = True
            for k, l in restrictions:
                if unionfind.find(k) == unionfind.find(i) and unionfind.find(j) == unionfind.find(l):
                    cond = False
                    break
                if unionfind.find(k) == unionfind.find(j) and unionfind.find(i) == unionfind.find(l):
                    cond = False
                    break
            results.append(cond)
            if cond:
                unionfind.union(i, j)
                
        return results        
        
        
        
            