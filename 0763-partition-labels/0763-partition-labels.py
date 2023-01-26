class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        words = Counter(s)
        left = 0
        letters = set()
        res = []
        
        for right in range(len(s)):
            
            letters.add(s[right])
            
            tempo = 0
            for letter in letters:
                tempo += words[letter]
            
            if tempo == right - left + 1:
                left = right + 1
                letters= set()
                res.append(tempo)
                
        return res