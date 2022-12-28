class Solution:
    def stoneRemover(self, num):
        return math.floor(num/2)
    
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = 0
        my_heap = []
        
        for i in range(len(piles)):
            total += piles[i]
            heapq.heappush(my_heap, -1 * piles[i])
        
        while k>0:
            curr = -1 * heapq.heappop(my_heap)
            divided = self.stoneRemover(curr)
            
            
            heapq.heappush(my_heap, -1 * (curr - divided))
            total -= divided
            k-=1
        
        return total
        
        