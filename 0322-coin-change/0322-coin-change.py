class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        
        def dfs(currCoin):
            if currCoin < 0:
                return math.inf
            if currCoin == 0:
                return 0
            if currCoin in memo:
                return memo[currCoin]
            
            count = 1
            temp = math.inf
            
            for ind in range(len(coins)):
                nxt= currCoin - coins[ind]
                temp = min(dfs(nxt) + count, temp)
                
            memo[currCoin] = temp
            return temp
        
        ans = dfs(amount)
        
        if ans < inf:
            return ans
        return -1