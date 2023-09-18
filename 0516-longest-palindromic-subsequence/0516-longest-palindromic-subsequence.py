class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def dp(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            
            if s[i] == s[j]:
                return dp(i + 1, j -1 ) + 2
            
            j_equiv = i
            
            while s[j_equiv] != s[j]:
                j_equiv += 1
            
            
            opt1, opt2 = 1, 1
            if j_equiv != j:
                opt1 = dp(j_equiv + 1, j - 1) + 2
            
            i_equiv = j
            while s[i_equiv] != s[i]:
                i_equiv -= 1
            
            if i_equiv != i:
                opt2 = dp(i + 1, i_equiv - 1) + 2
            
            opt3 = dp(i + 1, j - 1)
            return max(opt1, opt2, opt3)
        
        return dp(0, len(s) - 1)