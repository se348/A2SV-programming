class Solution:
    def numberOfWays(self, s: str) -> int:
        
        one_count_pref = []
        curr_one_count = 0        
        
        for i in range(len(s)):
            if s[i] == '1':
                curr_one_count += 1
            one_count_pref.append(curr_one_count)
        
        
        curr_one_count = 0
        res = 0
        
        for i in range(len(s) - 1, -1, -1):
            
            moved = len(s) -i
            
            if s[i] == '1':
                curr_one_count += 1
                res += (moved - curr_one_count) * (i + 1 -  one_count_pref[i])    
            
            else:
                res += curr_one_count * one_count_pref[i]
        
        return res