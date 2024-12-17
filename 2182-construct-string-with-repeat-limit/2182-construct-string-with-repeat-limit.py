class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = Counter(s)
        
        heap = []
        
        for key, value in counts.items():
            
            sub = ord('z') - ord(key)
            heappush(heap, (sub, key, value))
            
        res = []
        
        while heap:
            sub, char, value = heappop(heap)
            
            if res and res[-1] == char and value:
                if not heap:
                    break
                sub_next, char_next, value_next = heappop(heap)
                res.append(char_next)
                
                if value_next > 1:
                    heappush(heap, (sub_next, char_next, value_next - 1))
            
            mod = value % repeatLimit 
            iters = value // repeatLimit
            
            if iters:
                res.extend([char] * repeatLimit)
                heappush(heap, (sub, char, (iters - 1) * repeatLimit + mod))

            elif mod:
                res.extend([char] * mod)
                
        return "".join(res)