class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        mask =2
        prev= n & 1
        while mask <= n:
            currNum = mask & n
            curr = currNum == mask
            if curr == prev: return False
            prev = curr
            mask <<= 1
            
        return True