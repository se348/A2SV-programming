from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low =1
        high= 10**14 + 10
        while low<high:
            mid =(low+high)//2
            val = self.findTripGivenTime(time, mid)
            if val<totalTrips:
                low=mid+1
            else:
                high=mid
        return low
    def findTripGivenTime(self, time:List[int], indiv_time:int):
        total=0
        for i in time:
            total += (indiv_time//i)
        return total
s= Solution()
a= s.minimumTime([5,10,10],9)
print(a)