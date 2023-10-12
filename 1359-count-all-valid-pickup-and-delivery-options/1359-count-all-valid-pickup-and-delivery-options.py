class Solution:
    def countOrders(self, n: int) -> int:
        mod = (10 ** 9) + 7
        count = factorial(2 * n)
        res = count // pow(2, n )
        return int(res % mod)
        