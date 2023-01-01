class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        sett = set(spaces)
        for index in range(len(s)-1, -1, -1):
            
            if index in sett:
                res.append(" " + s[index])
            
            else:
                res.append(s[index])
                
        return "".join(reversed(res))