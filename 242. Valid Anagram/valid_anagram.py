from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countA = Counter(s)
        countB = Counter(t)
        return countA == countB