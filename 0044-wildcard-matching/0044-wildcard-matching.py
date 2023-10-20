class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        
        @cache
        def dp(s_ind, p_ind):
            if s_ind >= len(s) and p_ind >= len(p):
                return True
            
            if s_ind >= len(s):
                for i in range(p_ind, len(p)):
                    if p[i] != "*":
                        return False
                return True
            if p_ind >= len(p):
                for i in range(s_ind, len(s)):
                    if s[i] != "*":
                        return False
                return True
            
            if s[s_ind] != "*" and s[s_ind] == p[p_ind]:
                return dp(s_ind + 1, p_ind + 1)
            
            if s[s_ind] == "?" or p[p_ind] == "?":
                return dp(s_ind + 1, p_ind + 1)
            
            
            if s[s_ind] == "*":
                if dp(s_ind, p_ind + 1) or dp(s_ind + 1, p_ind + 1) or dp(s_ind + 1, p_ind):
                    return True
                
                
            if p[p_ind] == "*":
                if dp(s_ind + 1, p_ind) or dp(s_ind + 1, p_ind + 1) or dp(s_ind, p_ind + 1):
                    return True
                
            
            return False
        
       
        return dp(0,0)