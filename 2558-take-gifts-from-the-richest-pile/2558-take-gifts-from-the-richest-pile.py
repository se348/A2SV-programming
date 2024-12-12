class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        for i in range(len(gifts)):
            gifts[i] *= -1
            
        heapify(gifts)
        for i in range(k):
            curr_val = heapq.heappop(gifts)
            curr_val *= -1
            
            root = sqrt(curr_val)
            root = floor(root)
            heapq.heappush(gifts, -root)
            
        return -sum(gifts)