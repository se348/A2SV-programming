class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        
        is_prime = [True] * (n + 1)
        is_prime[1] = False
        
        primes = []
        
        for i in range(2, n + 1):
            if not is_prime[i]:
                continue
            
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
            
            primes.append(i)
        
        res = []
        
        prime_set = set(primes)
        
        for num in primes:
            if n - num in prime_set and  num <=  n - num:
                res.append((num, n - num))
        
        return res
        