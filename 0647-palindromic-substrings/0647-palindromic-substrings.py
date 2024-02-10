class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        
        for i in range(len(s)):
            
            left_movt= i
            right_movt = i + 1
            
            while left_movt >= 0 and right_movt < len(s) and s[left_movt] == s[right_movt]:
                left_movt -= 1
                right_movt += 1
                count += 1
            
            left_movt = i
            right_movt = i
            
            while left_movt >= 0 and right_movt < len(s) and s[left_movt] == s[right_movt]:
                left_movt -= 1
                right_movt += 1
                count += 1
        
        return count