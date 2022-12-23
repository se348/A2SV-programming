class Solution:
    def check(self, word1, word2, sorter):
        length = min(len(word1), len(word2))
        i = 0
        while i < length:
            if sorter[word1[i]]< sorter[word2[i]]:
                return True
            elif sorter[word1[i]]> sorter[word2[i]]:
                return False
            else:
                i+=1
        if i< len(word1):
            return False
        return True
            
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        sorter = {}
        for i, charachter in enumerate(order):
            sorter[charachter] = i
        for i in range(len(words)-1):
            if self.check(words[i], words[i+1], sorter):
                continue
            else:
                return False
        return True