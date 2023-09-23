class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_diction = Counter(t)
        
        unsatisfied = len(t_diction)
        left_ptr = 0
        s_counter= defaultdict(int)
        res, starter, end = math.inf, math.inf, math.inf
        
        
        for right_ptr in range(len(s)):
            if s[right_ptr] not in t_diction:
                continue
            
            current = s[right_ptr]
            s_counter[current] += 1
            if s_counter[current] == t_diction[current]:
                unsatisfied -= 1
                
            while unsatisfied == 0 and left_ptr <= right_ptr:
                if (right_ptr - left_ptr + 1) < res:
                    res = (right_ptr - left_ptr + 1)
                    starter = left_ptr
                    end = right_ptr + 1
                 
                if s[left_ptr] in t_diction:
                    s_counter[s[left_ptr]] -= 1

                    if  s_counter[s[left_ptr]] < t_diction[s[left_ptr]]:
                        unsatisfied += 1

                left_ptr += 1
                
        if res == inf:
            return ""
        
        return s[starter: end]
            
            
            
        