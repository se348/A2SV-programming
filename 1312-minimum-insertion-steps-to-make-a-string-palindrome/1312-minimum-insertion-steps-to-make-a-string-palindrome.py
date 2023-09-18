class Solution:
    def minInsertions(self, s: str) -> int:
        
        @cache
        def dp(i, j):
            if i >= j:
                return 0
            elif s[i] == s[j]:
                return dp(i + 1, j - 1)
            
            choice1 = dp(i + 1, j) + 1
            choice2 = dp(i, j - 1) + 1
            
            return min(choice1, choice2)
        
        return dp(0, len(s) -1)
            