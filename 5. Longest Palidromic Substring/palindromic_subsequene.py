class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        ans =0
        soln=""
        for i , n in enumerate(s):
            j=i
            k=i
            while j>=0 and k<len(s):
                if s[j] == s[k]:
                    if ans < k-j+1:
                        ans =k-j+1
                        soln = s[j:k+1]
                else:
                    break
                j-=1
                k+=1
            j=i
            k=i+1
            while j>=0 and k<len(s):
                if s[j] == s[k]:
                    if ans < k-j+1:
                        ans =k-j+1
                        soln = s[j:k+1]
                else:
                    break
                j-=1
                k+=1
        return soln
                        