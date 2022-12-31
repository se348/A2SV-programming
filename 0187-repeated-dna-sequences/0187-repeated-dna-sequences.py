class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if len(s) < 10:
            return []
        
        sett = set()
        result = set()
        
        for i in range(9, len(s)):
            
            if s[i-9: i+1] in sett:
                result.add(s[i-9: i+1])
            
            else:
                sett.add(s[i-9: i+1])    
        
        return list(result)