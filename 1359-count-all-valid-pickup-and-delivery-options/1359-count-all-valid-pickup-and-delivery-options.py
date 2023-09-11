class Solution:
    def countOrders(self, n: int) -> int:
        
        res = 1
        mod = 10 ** 9 + 7
        for i in range(1, n + 1):
            multiple = 2 * i
            res *= (multiple * (multiple - 1) / 2)
            res %= mod
        return int(res)