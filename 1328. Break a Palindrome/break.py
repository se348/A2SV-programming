class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        pal = ""
        for s in palindrome:
            pal+=s
        count=0
        for ind, char in enumerate(palindrome):
            if char!="a" and count==0:
                pal= palindrome[:ind]+ "a" + palindrome[ind+1:]
                count+=1
                break
        if len(pal)==1:
            return ""
        if pal != pal[::-1]: 
            return pal
        for i in range(len(palindrome)-1,-1,-1):
            if palindrome[i]=="a":
                palindrome=palindrome[:i]+ "b" + palindrome[i+1:]
                break
        return palindrome
        