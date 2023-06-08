class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kElementNums = []
        self.k = k
        for num in nums:
            if len(self.kElementNums) < k:
                heapq.heappush(self.kElementNums, num)
                
            else:
                currSmallest = self.kElementNums[0]
                if num > currSmallest:
                    heapq.heappop(self.kElementNums)
                    heapq.heappush(self.kElementNums, num)

    def add(self, val: int) -> int:
        if not self.kElementNums:
            heapq.heappush(self.kElementNums, val)
            return self.kElementNums[0]
        
        currSmallest = self.kElementNums[0]
        
        if val > currSmallest and len(self.kElementNums) == self.k:
            heapq.heappop(self.kElementNums)
            heapq.heappush(self.kElementNums, val)
            
        elif len(self.kElementNums) < self.k:
            heapq.heappush(self.kElementNums, val)
        
        return self.kElementNums[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)