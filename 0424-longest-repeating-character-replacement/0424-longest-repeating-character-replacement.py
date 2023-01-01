class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        diction = defaultdict(int)
        slow_ptr = 0
        result = 0
        diction[s[0]] = 1
        
        for fast_ptr in range(1, len(s)):
            
            diction[s[fast_ptr]] += 1
            replacements = fast_ptr - slow_ptr +1 - max(diction.values())
        
            if replacements < k:
                result = max(result, fast_ptr - slow_ptr + 1)
            
            elif replacements == k:
                result = max(result, fast_ptr - slow_ptr + 1)
                
            else:
                while slow_ptr<=fast_ptr and fast_ptr - slow_ptr +1 - max(diction.values()) > k:

                    cond = True
                    diction[s[slow_ptr]] -= 1
                    slow_ptr += 1
            
                result = max(result, fast_ptr - slow_ptr + 1)
                
        return result