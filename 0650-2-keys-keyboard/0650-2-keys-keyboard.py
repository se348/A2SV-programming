class Solution:
   
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        res= 0 
        dp= [i for i in range(n + 1)]
        
        for i in range(3, n+ 1):
            for j in range(1, i + 1):
                if (i % j == 0):
                    multiples = (i// j)
                    dp[i] = min(dp[i], dp[j] + multiples)
        
        return dp[n]
                                
            
