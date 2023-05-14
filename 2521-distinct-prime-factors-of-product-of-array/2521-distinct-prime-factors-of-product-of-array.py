class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        nums.sort()
        traversed = set()
        
        primes = set()
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in traversed or nums[i] in primes:
                continue
            d = 2
            while nums[i] >= d:
                while nums[i] %d == 0:
                    primes.add(d)
                    nums[i] //=d
                    traversed.add(nums[i])
                d += 1
                
        return len(primes)