class Solution:
    def fib(self, n: int) -> int:
        memo ={}
        def helper(n):
            if n==0:
                return 0
            if n==1:
                return 1
            if n in memo:
                return memo[n]
            ans = helper(n-1) + helper(n-2)
            memo[n]= ans
            return ans
        return helper(n)