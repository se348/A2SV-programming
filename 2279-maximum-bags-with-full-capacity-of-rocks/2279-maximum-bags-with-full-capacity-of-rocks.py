class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = []
        for i in range(len(rocks)):
            heapq.heappush(diff,capacity[i]- rocks[i])
        
        k=0
        count= 0
        print(diff)
        while True:
            if not diff:
                return count
            curr = heapq.heappop(diff)
            if curr==0:
                count+=1
            elif curr<=additionalRocks:
                additionalRocks-=curr
                count+=1
            else:
                return count
                