class Solution:
    def countHomogenous(self, s: str) -> int:
        counter = 0
        length = len(s)
        right = 0
        left = 0
        
        while left < length:
            
            while right < len(s) and s[left] == s[right]:
                right += 1
            
            n = right - left
            counter += (n * (n + 1) // 2)
            left = right
            
        return (counter % ((10 ** 9) + 7))
        