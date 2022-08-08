from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l ,r = 0, len(citations)
        ans= -1
        while l<=r:
            mid =(l +r)//2
            if self.checkCitations(citations, mid):
                ans=max(mid, ans)
                l= mid+1
            else:
                r =mid-1
        return ans
            
    
    
    def checkCitations(self,citations, num):
        count =0
        for n in citations:
            if n>=num:
                count+=1
        return count>=num


