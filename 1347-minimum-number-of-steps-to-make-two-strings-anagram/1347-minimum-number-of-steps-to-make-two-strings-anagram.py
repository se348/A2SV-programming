class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        t_counter = Counter(t)
        s_counter = Counter(s)
        
        a = 0
        
        for i in range(26):
            key = chr(ord('a') + i)
            temp =( t_counter[key] - s_counter[key])
            
            if temp > 0:
                a += temp
        
        return a
            