class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
       
        @cache
        def dfs(curr_amount, n):
            if curr_amount < 0:
                return 0
            if curr_amount == 0:
                return 1
            
            res = 0
            
            for i in range(n):
                res += dfs(curr_amount - coins[i], i + 1)
            
            return res
        
        return dfs(amount, len(coins))