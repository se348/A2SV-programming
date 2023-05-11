class Solution:
    def findComplement(self, num: int) -> int:
        
        result = 0
        mask = 1
        
        while num > 0:
            if not (num & 1):
                result += mask
            mask *= 2
            num = num >> 1
        return result