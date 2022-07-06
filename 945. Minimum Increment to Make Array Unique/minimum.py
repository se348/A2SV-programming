from typing import List
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count =0
        for i, n in enumerate(nums):
            if i==0:
                continue
            if nums[i] <=nums[i-1]:
                difference = -(nums[i] -(nums[i-1]+1))
                nums[i]+= difference
                count+= difference
        return count


s= Solution()
s.minIncrementForUnique([3,2,1,2,1,7])