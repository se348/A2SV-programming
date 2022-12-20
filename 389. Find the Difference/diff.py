class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        set_a =collections.defaultdict(int)
        set_b=collections.defaultdict(int)
        for char in s:
            set_a[char]+=1
        for char in t:
            set_b[char]+=1
        for char in t:
            if set_a[char] != set_b[char]:
                return char
        