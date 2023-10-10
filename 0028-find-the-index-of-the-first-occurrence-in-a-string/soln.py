class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        hashed_needle = 0
        alpha = 27
        
        hashed_haystack = 0
        
        for i in range(len(needle)):
            prev = (hashed_needle * 27)
            current = (ord(needle[i]) - 96)
            hashed_needle =  prev + current
            
            prev = (hashed_haystack * 27) 
            current = (ord(haystack[i]) - 96)
            hashed_haystack =  prev + current
        
        if hashed_haystack == hashed_needle:
            return 0
        
        for i in range(1, len(haystack) - len(needle) + 1):
           
            
            a = len(needle) - 1
            b = ord(haystack[i - 1]) - 96
            removed = (b * (alpha** a ))
            hashed_haystack -= removed
            
            
            curr_ind = i + len(needle) 
            prev = (hashed_haystack * 27) 
            current = (ord(haystack[curr_ind - 1]) - 96)
            hashed_haystack =  prev + current
            
            
            if hashed_haystack == hashed_needle:
                return curr_ind - len(needle)
        return -1 
