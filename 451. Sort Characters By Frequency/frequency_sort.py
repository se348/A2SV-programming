from collections import Counter
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        llist =[]
        for i in count:
            a =count.get(i)
            heapq.heappush(llist,(-1 * a,i))
        ans=""
        while llist:
            a =heapq.heappop(llist)
            b =a[1] *(-1 *a[0])
            ans+=b
        return ans