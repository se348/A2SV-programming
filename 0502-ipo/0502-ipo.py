class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_heap = []
        
        for i in range(len(capital)):
            heapq.heappush(min_heap, (capital[i], profits[i]))
            
        max_heap = []
        while k:
            
            while min_heap and min_heap[0][0] <= w:
                c, p = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (-p, c))
            
            if max_heap:
                curr_p, curr_c = heapq.heappop(max_heap)
                curr_p *= -1
                w += curr_p
            k-= 1
                
        return w