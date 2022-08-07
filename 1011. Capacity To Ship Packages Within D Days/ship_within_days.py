from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r= sum(weights)
        ans=-1
        while l<=r:
            mid =(l+r)//2
            if self.checkIfPossible(weights, days,mid):
                ans= mid
                r= mid-1
            else:
                l=mid+1
        return ans
        
        
        
    def checkIfPossible(self, weighs: List[int], days :int, capacity: int):
        value= capacity
        i=0
        while i< len(weighs):
            if value>=weighs[i]:
                value-=weighs[i]
                i+=1
            else:
                if days>1:
                    days-=1
                    value = capacity
                else: return False
        return True

s =Solution()
a = s.shipWithinDays([3,2,2,4,1,4],3)
print(a)