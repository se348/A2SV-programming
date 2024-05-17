class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
#         @cache
#         def dp(s_ind, t_ind):
#             if t_ind == len(t):
#                 return 1
#             if s_ind == len(s):
#                 return 0
            
#             if s[s_ind] == t[t_ind]:
#                 return dp(s_ind + 1, t_ind + 1) + dp(s_ind + 1, t_ind)
            
#             return dp(s_ind + 1, t_ind)
        
#         return dp(0, 0)
        
        # dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
        dp = [[0]*(len(t)+1) for i in range(len(s)+1)]
        
        for i in range(len(s)+1):
            dp[i][len(t)] = 1
        
        for j in range(len(t)-1, -1, -1):
            for i in range(len(s)-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
                dp[i][j] += dp[i+1][j]
        # print(dp)
        return dp[0][0]
                
            