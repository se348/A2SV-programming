from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit =0
        for i in prices:
            buy=min(buy, i)
            profit=max(profit, i-buy)
        return profit