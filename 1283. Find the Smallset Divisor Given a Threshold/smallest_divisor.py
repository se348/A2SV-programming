from math import ceil
import random
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low =1
        high= max(nums)
        result = 1
        while low<high:
            mid= (low+high)//2
            if self.find_sum(nums, mid)> threshold:
                low=mid+1
                result= low
            else:
                high= mid
                result= mid
                if mid>1:
                    immediate_smaller = self.find_sum(nums, mid-1)
                    if immediate_smaller>threshold:
                        return mid
        return result
                
        
        
        
    def find_sum(self, nums:List[int], divisor:int):
        total =0
        for n in nums:
            total += ceil(n/divisor)
        return total

s= Solution()
d= s.smallestDivisor([44,22,33,11,1],5)
print(d)