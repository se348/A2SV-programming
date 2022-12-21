class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        w1 = len(word1)
        w2 = len(word2)
        res= ""
        while i< min(w1, w2):
            curr= word1[i]+ word2[i]
            res+=curr
            i+=1
        while i<len(word1):
            res+=word1[i]
            i+=1
        while i<len(word2):
            res+=word2[i]
            i+=1
        return res