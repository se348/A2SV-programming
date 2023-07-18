class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        min_heap = []
        
        for i in counter:
            
            if len(min_heap) == k and  counter[i] > min_heap[0][0]:
                heapq.heappop(min_heap)
            
            if len(min_heap) < k: 
                heapq.heappush(min_heap, (counter[i], i))
        
        
        result = []
        
        for i, j in min_heap:
            result.append(j)
            
        return result