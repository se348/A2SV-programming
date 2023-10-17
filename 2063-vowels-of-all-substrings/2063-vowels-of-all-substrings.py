class Solution:
    def countVowels(self, word: str) -> int:
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        
        res = 0
        length = len(word)
        
        for i in range(length):
            if word[i] in vowels:
                res += (i + 1) * (length- i)
        return res
        