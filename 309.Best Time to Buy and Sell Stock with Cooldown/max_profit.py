from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        def dfs(index, have=False):
            if (index,have) in memo:
                return memo[(index,have)]
            if index>=len(prices):
                return 0
            if have==False:
                buy = dfs(index+1, True ) - prices[index]
                res_cool =  dfs(index+1, False)
                memo[(index,have)] =max(buy, res_cool)
                return max(buy, res_cool)
            else:
                res_sell = dfs(index+2, False) + prices[index]
                res_cool =  dfs(index+1, True)
                memo[(index,have)] =  max(res_sell, res_cool)
                return max(res_sell, res_cool)
        return dfs(0)