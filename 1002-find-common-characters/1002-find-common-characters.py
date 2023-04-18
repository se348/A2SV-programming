class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = []
        
        for word in words:
            count.append(dict(Counter(word)))
        
        
        res = []
        for i in range(26):
            char = 97 + i
            temp = chr(char)
            curr = math.inf
            
            for ind in range(len(words)):
                curr = min(count[ind].get(temp,0), curr)
            for j in range(curr):
                res.append(temp)
        print(res)
        return res