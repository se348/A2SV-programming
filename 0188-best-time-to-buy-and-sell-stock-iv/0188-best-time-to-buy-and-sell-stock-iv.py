class Solution:
    def maxProfit(self, k: int, prices: List[int]):
        @cache
        def dfs(ind, k, have=False):
            if ind>=len(prices):
                return 0
            if k<0:
                return 0
            if have==False:
                a= dfs(ind+1, k-0.5, True) -prices[ind]
                b= dfs(ind+1, k, False)
                return max(a,b)
            else:
                a= dfs(ind+1, k-0.5, False) +prices[ind]
                b=dfs(ind+1, k, True)
                return max(a,b)
        return dfs(0,k)
            
            