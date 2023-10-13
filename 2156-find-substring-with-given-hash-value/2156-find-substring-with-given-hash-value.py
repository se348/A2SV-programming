class Solution:
#     def multiply(self, a, b, m):
#         return ((a % m) * (b % m)) % m
#     def binary_exponentiation(self, base, exponent, mod):
#         result = 1
#         while exponent > 0:
#             if exponent & 1:
#                 result = self.multiply(base, result, mod)
#             base = self.multiply(base, base, mod) 
#             exponent >>= 1
#         return result
    
#     def division(self, a, b, mod):
#         return self.multiply(a, self.inverse(b, mod), mod)
    
#     def inverse(self, a, mod):
#         return self.binary_exponentiation(a, mod - 2, mod)
    
    
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        s = s[::-1]
        curr_hash = 0
        
        ans = ""
        
        ptr = k-1
        for i in range(k):
            curr_letter = ord(s[i]) - 96
            curr_hash = (curr_hash + (curr_letter * pow(power, ptr, modulo))) % modulo
            ptr -= 1
            
        if curr_hash == hashValue:
            ans = s[:k][::-1]
    
        start= 0
        
        for i in range(k, len(s)):
            curr_letter = ord(s[start]) - 96
            curr_hash = (curr_hash - (curr_letter * pow(power, k - 1, modulo))) % modulo
            curr_hash = (curr_hash * power) % modulo 
            
            curr_hash += ord(s[i]) - 96
            
            curr_hash %= modulo
            
            if curr_hash == hashValue:
                ans= s[start + 1: i + 1][::-1]
            
            start += 1
        return ans
    
            
            
        