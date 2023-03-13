class Solution:
    def custompow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 4 == 0:
            return self.custompow(x, n// 4) ** 4
        if n % 2 == 0:
            return self.custompow(x, n// 2) ** 2
        return (self.custompow(x, n//2) ** 2) * x        
   
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.custompow(1 /x, abs(n))
        
        return self.custompow(x, n)
        