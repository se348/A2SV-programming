class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s =s.strip()
        a =s.split()
        return len(a[-1])