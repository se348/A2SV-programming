class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        curr_heap = []
        
        for stone in stones:
            heapq.heappush(curr_heap, -1 * stone)
            
        while len(curr_heap) > 1:
            y = - heapq.heappop(curr_heap)
            x = - heapq.heappop(curr_heap)
            
            if x != y:
                heapq.heappush(curr_heap, x - y)
                
        if not curr_heap:
            return 0
        return - curr_heap[0]
        