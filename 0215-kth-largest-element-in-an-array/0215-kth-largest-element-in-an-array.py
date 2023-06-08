class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kContainingHeap = []
        
        for num in nums:
            if len(kContainingHeap) < k:
                heapq.heappush(kContainingHeap, num)
                
            else:
                small = kContainingHeap[0]
                if num > small:
                    heapq.heappop(kContainingHeap)
                    heapq.heappush(kContainingHeap, num)
                    
        return kContainingHeap[0]
                    