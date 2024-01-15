class Solution:
    def addMinimum(self, word: str) -> int:
        
        res = 0
        
        for i in range(len(word)):
        
            if word[i] == 'b':
                
                if i == 0 or word[i - 1] == 'c':
                    res += 1
                elif word[i - 1] =='b':
                    res += 2
                    
            elif word[i] == 'c':
                
                if i == 0 or word[i - 1] == 'c':
                    res += 2
                
                elif word[i - 1] == 'a':
                    res += 1
                
            elif word[i] == 'a' and i != 0:
                if word[i - 1] == "b":
                    res += 1
                
                elif word[i - 1] == 'a':
                    res += 2
        
        if word[-1] == 'b':
            res += 1
        elif word[-1] == "a":
            res += 2
        
        return res
                    