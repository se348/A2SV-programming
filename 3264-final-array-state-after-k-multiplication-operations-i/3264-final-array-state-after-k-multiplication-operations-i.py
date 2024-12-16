class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        arr = [(nums[i], i) for i in range(len(nums))]
        
        heapify(arr)
        
        for _ in range(k):
            val, ind = heapq.heappop(arr)
            
            heappush(arr, (val * multiplier, ind))
            
        
        arr.sort(key=lambda a: a[1])
        
        res = [a for a, _ in arr]
        
        return res