class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1:1}
        
        def dfs(curr):
            if curr in memo:
                return memo[curr]
            temp = dfs(curr - 1) + dfs(curr -2)
            memo[curr] = temp
            return temp
        
        return dfs(n)
        