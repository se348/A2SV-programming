from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count =sum(nums)
        count2 =sum(range(len(nums)+1))
        return count2 -count
        
        