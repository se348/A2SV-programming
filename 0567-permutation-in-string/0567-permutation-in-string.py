class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        length_s1 = len(s1)
        length_s2 = len(s2)
        
        if length_s1 > length_s2:
            return False
        
        target_window = Counter(s1)
        curr_window = Counter(s2[:length_s1])

        if target_window == curr_window:
            return True

        for i in range(length_s2 - length_s1):
            curr_window[s2[i]] -= 1
            
            if curr_window[s2[i]] == 0:
                del curr_window[s2[i]]
                
            curr_window[s2[i  + length_s1]] += 1
        
            if target_window == curr_window:
                return True
            
        return False