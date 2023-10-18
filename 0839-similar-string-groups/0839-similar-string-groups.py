class UnionFind:
    def __init__(self, strs):
        self.parent= {}
        self.rank = defaultdict(int)
        
        for chars in strs:
            self.parent[chars] = chars
    
    def find(self, curr_str):
        if self.parent[curr_str] == curr_str:
            return curr_str
        
        self.parent[curr_str] = self.find(self.parent[curr_str])
        return self.parent[curr_str]
    
    def union(self, curr_str1, curr_str2):
        par1, par2 = self.find(curr_str1), self.find(curr_str2)
        rank1, rank2 = self.rank[par1], self.rank[par2]
        if par1 == par2:
            return
        if rank1 <= rank2:
            self.parent[par2] = self.parent[par1]
            self.rank[par2] += self.rank[par1]
        
        else:
            self.parent[par1] = self.parent[par2]
            self.rank[par1] += self.rank[par2]
        
class Solution:
    def isAllowed(self, curr_str1, curr_str2):
        
        a ,b = "", ""
        no_more_allowed = False
        
        for i in range(len(curr_str1)):
            
            if curr_str1[i] == curr_str2[i]:
                continue
            if no_more_allowed:
                return False
            if not a:
                a , b = curr_str1[i], curr_str2[i]
            else:
                if a == curr_str2[i] and b == curr_str1[i]:
                    no_more_allowed = True
                else:
                    return False
        return True                    
            
        
        
    def numSimilarGroups(self, strs: List[str]) -> int:
        disjointSet = UnionFind(strs)
        length = len(strs)
        
        for i in range(length):
            for j in range(i + 1, length):
                
                if self.isAllowed(strs[i], strs[j]):
                    disjointSet.union(strs[i], strs[j])
        
        uniques = set()
        
        for i in range(length):
            uniques.add(disjointSet.find(strs[i]))
        
        return len(uniques)
            