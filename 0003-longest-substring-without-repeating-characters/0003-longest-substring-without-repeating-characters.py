class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        window = {}
        maxlen = 0
        
        for end in range(len(s)):
            if s[end] in window and window[s[end]] >= start:
                start = window[s[end]] + 1
            
            window[s[end]] = end
            maxlen = max(maxlen, end- start + 1)
        
        return maxlen