class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==1:
            return 1
        if x==-1 and abs(n)%2==1:
            return -1
        if x==-1 and abs(n)%2==0:
            return 1
        if n==0:
            return 1 
        if n< 0:
            if n< -100000:
                return 0.0
            d =self.helper(x, abs(n))
            return 1 / d
        return self.helper(x, n)
    def helper(self, x, n):
        if n==1:
            return x
        if n==0:
            return 1
        if n%2==1:
            return (self.helper(x, n//2) ** 2) * x
        return (self.helper(x, n//2) ** 2)
