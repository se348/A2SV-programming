class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        new_rev = []
        
        for char in s:
            if char.isalpha():
                new_rev.append(char)
                
        new_rev.reverse()
        
        
        res = []
        counter = 0
        for i in range(len(s)):
            char =s[i]
            if not char.isalpha():
                res.append(char)
            else:
                res.append(new_rev[counter])
                counter += 1
        return "".join(res)