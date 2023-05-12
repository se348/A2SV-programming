class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        
        prime = 2
        
        while prime <= n:
            while n % prime ==0:
                res += prime
                n //= prime
            prime += 1
            
        return res