class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        choices = [2,3,5]
        heap = [2,3,5]
        n -= 1
        visited = {2,3,5}
        res = -1
        
        while n:
            currnum = heapq.heappop(heap)
            res = currnum
            
            for choice in choices:
                if currnum * choice not in visited:
                    visited.add(currnum * choice)
                    heapq.heappush(heap, currnum * choice)
            n -=1
        return res