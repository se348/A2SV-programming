class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        dp = [([inf] * (m + 1)) for _ in range(n + 1)]
        
        dp[0][0] = 0
        
        for i in range(n + 1):
            for j in range(m + 1):
                
                if i == 0 and j == 0:
                    continue
                    
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + 1
                
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + 1
                    
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    
        return dp[-1][-1]
        
        
        