class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        
        def dp(ind, haveStock):
            if ind >= len(prices):
                return 0
            if (ind, haveStock) in memo:
                return memo[(ind, haveStock)]
            
            if haveStock:
                option1 = dp(ind + 1, False) + (prices[ind] - fee)
                option2 = dp(ind + 1, True) 
                
            else:
                option1 = dp(ind + 1, True) - prices[ind]
                option2 = dp(ind + 1, False)
                
            memo[(ind, haveStock)] = max(option1, option2)
            return max(option1, option2)

        return dp(0, False)