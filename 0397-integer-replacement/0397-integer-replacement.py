class Solution:
    def integerReplacement(self, n: int) -> int:
        dp = {}
        
        def dfs(curr):
            if curr > n * 2 or curr < 0:
                return inf
            if curr == 1:
                return 0
            if curr in dp:
                return dp[curr]
            
            nxt1, nxt2, nxt3 =inf, inf, inf
            if curr & 1 ==0:
                nxt1 = dfs(curr // 2)
            else:
                nxt2 = dfs(curr - 1)
                nxt3 = dfs(curr + 1)
            
            res = 1 + min(nxt1, nxt2, nxt3)
            dp[curr] =res
            return dp[curr]
        
        return dfs(n)