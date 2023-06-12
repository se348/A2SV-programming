class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a != 0:
            heappush(max_heap, (-a, 'a'))
        if b != 0:
            heappush(max_heap, (-b, 'b'))
        if c != 0:
            heappush(max_heap, (-c, 'c'))
        res = []
        
        while max_heap:
            first, char1 = heappop(max_heap)
            if len(res) >= 2 and res[-1] == res[-2] == char1: 
                if not max_heap: 
                    return ''.join(res)
                second, char2 = heappop(max_heap) 
                res.append(char2)
                second += 1 
                if second != 0:
                    heappush(max_heap, (second, char2))
                heappush(max_heap, (first, char1)) 
                continue
			
            res.append(char1)
            first += 1
            if first != 0:
                heappush(max_heap, (first, char1))
                
        return ''.join(res)
            
        