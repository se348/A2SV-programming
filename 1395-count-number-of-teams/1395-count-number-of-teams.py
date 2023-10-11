class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        dp = [[0,0] for i in rating]
        
        length = len(rating) 
        
        
        res = 0
        
        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                if rating[j] > rating[i]:
                    res += dp[j][0] 
                    dp[i][0] += 1
                
                else:
                    res += dp[j][1] 
                    dp[i][1] += 1
        return res