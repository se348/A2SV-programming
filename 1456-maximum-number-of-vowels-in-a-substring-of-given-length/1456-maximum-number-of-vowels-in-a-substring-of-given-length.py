class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0 
        vowels = {"a", "e", "i", "o", "u"}
        
        for i in range(k):
            if s[i] in vowels:
                count += 1
        
        length = len(s)
        
        result = count
        
        for j in range(k, length):
            if s[j] in vowels:
                count += 1
            if s[j - k] in vowels:
                count -= 1
            result = max(result, count)
        
        return result
                
            