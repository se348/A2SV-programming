class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        n = len(b)
        curr =1
        res= 1
        mod = 1337
        
        for i in range(n - 1, -1, -1):
            multiple = (curr * b[i])
            temp = pow(a , multiple, mod)
            res *= temp
            res %= mod
            curr *= 10
        
        return res    
        