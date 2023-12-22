class Solution:
    def bulbSwitch(self, n: int) -> int:
        i = 1
        
        while (i ** 2) <= n:
            i += 1
        
        return i - 1
        