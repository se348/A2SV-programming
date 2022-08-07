from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l , r =1, len(nums)
        ans=-1
        while l<=r:
            mid =(l+r)//2
            
            count =0
            for n in nums:
                if n<=mid:
                    count+=1
            if count> mid:
                ans = mid
                r= mid-1
            else:
                l=mid+1
        return ans