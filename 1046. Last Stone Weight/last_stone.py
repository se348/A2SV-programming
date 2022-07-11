import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones=[]
        for n in stones:
            new_stones.append(-1 * n)
        heapq.heapify(new_stones)
        while len(new_stones) >1:
            y = heapq.heappop(new_stones)
            x= heapq.heappop(new_stones)
            if abs(x) == abs(y):
                continue
            else:
                heapq.heappush(new_stones, -1 * (abs(y)- abs(x)))
        if new_stones==[]:
            return 0
        return abs(new_stones[0])

s =Solution()
a =s.lastStoneWeight([9,10,1,7,3])
print(a)