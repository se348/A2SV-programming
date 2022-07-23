from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i= 0
        while i< len(nums):
            if i==0:
                i+=1
                continue
            if nums[i]==nums[i-1]:
                nums.pop(i)
            else:
                i+=1
        print(nums)
        return len(nums)


s= Solution()
s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
                