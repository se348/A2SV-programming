class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        
        def dp(ind):
            if ind >= len(s):
                return 1
            if ind in memo:
                return memo[ind]
            opt1, opt2 = 0,0
            
            if s[ind] != '0':
                opt1 = dp(ind + 1)
                if ind < len(s) - 1 and int(s[ind]) * 10 + int(s[ind+ 1]) <= 26:
                    opt2 = dp(ind +2)
            memo[ind] = opt1 + opt2
            return opt1 + opt2       
        return dp(0)
        