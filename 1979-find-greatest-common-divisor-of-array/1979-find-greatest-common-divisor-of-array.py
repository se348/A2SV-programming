class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a %b)
        minim =min(nums)
        maxim = max(nums)
        return gcd(maxim, minim)