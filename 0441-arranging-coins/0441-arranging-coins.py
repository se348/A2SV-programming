class Solution:
    def arrangeCoins(self, n: int) -> int:
        currNum = 0
        currSum = 0
        
        while currSum <= n:
            currNum += 1
            currSum += currNum
        return currNum - 1
        