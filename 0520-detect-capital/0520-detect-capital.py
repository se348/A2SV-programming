class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) ==1:
            return True
        
        val = word.islower() or word.isupper()
        return val or (word[1:].islower() and word[0].isupper) 