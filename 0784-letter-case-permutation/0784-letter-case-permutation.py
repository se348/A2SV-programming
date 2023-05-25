class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = set()
        
        num = 10011
        
        for i in range(pow(2, len(s))):
            bit = 1
            current = []
            for elem in s:
                current.append(elem)
                
            for j in range(len(s)):
                if i & bit:
                    current[j] = current[j].upper()
                else: 
                    current[j] = current[j].lower()
                bit <<= 1
                
            res.add("".join(current))
            
        return res