class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        monotonic_stack = []
        
        for idx, price in enumerate(prices):
            while monotonic_stack and monotonic_stack[-1][0] >= price:
                prev_price, prev_idx = monotonic_stack.pop()
                prices[prev_idx] = prev_price - price
            monotonic_stack.append((price, idx))
        return prices