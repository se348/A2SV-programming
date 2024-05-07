class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        
        @cache
        def dp(l, r):
            
            if l == r - 1:
                return 0
            
            if l == r - 2:
                return values[l] * values[r] * values[l + 1]
            
            ans = inf
            
            for i in range(l + 1, r):
                ans= min(dp(l, i) + dp(i, r) + (values[l] * values[r] * values[i]), ans)
                
            return ans
        
        return dp(0, len(values) - 1)