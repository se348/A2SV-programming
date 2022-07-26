class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return -1
        if len(needle)> len(haystack):
            return -1
        i= 0
        l =len(needle)
        while i < len(haystack):
            tempo = haystack[:i]+ needle + haystack[(i+l):]
            if tempo==haystack:return i
            i+=1
        return -1
s= Solution()
a =s.strStr("aaaa","bba")
print(a)