class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        
        
        a = list(counter1.items())
        b = list(counter2.items())
        
        a.sort(key= lambda g: g[1])
        b.sort(key= lambda g: g[1])
        
        for i in range(len(a)):
            
            if a[i][1] != b[i][1]:
                return False
            
            if a[i][0] not in counter2:
                return False
            
            if b[i][0] not in counter1:
                return False
            
        return True