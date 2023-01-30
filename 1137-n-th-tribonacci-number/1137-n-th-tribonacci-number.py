class Solution:
    def dp(self, num, memo):
        if num < 0:
            return 0
        elif num == 1:
            return 1
        elif num == 2:
            return 1
        elif num in memo:
            return memo[num]
        
        temp = self.dp(num-1, memo) + self.dp(num -2, memo) + self.dp(num -3, memo)
        memo[num] = temp
        return temp
    
    def tribonacci(self, n: int) -> int:
        memo ={}
        return self.dp(n, memo)    