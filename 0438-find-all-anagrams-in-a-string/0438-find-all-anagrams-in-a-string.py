class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_count = Counter(s[:len(p)]) 
        target_count = Counter(p)
        
        indices = []
        
        if window_count == target_count:
            indices.append(0)
        
        print(window_count)
        
        for i in range(len(s) - len(p)):
            window_count[s[i]] -= 1
            
            if window_count[s[i]] == 0:
                del window_count[s[i]]
                
            window_count[s[i + len(p)]] += 1
            
            if window_count == target_count:
                indices.append(i + 1)
                
            
        return indices