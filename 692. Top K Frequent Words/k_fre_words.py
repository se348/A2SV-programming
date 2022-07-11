from collections import Counter
import heapq
from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        llist =[]
        for n in count:
            llist.append((-1 *count[n], n))
        heapq.heapify(llist)
        soln=[]
        for n in range(k):
            soln.append(heapq.heappop(llist)[1])
        return soln

s =Solution()
a = s.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4)
print(a)