class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @cache
        def dp(s_ind, t_ind):
            if t_ind == len(t):
                return 1
            if s_ind == len(s):
                return 0
            
            if s[s_ind] == t[t_ind]:
                return dp(s_ind + 1, t_ind + 1) + dp(s_ind + 1, t_ind)
            
            return dp(s_ind + 1, t_ind)
        
        return dp(0, 0)