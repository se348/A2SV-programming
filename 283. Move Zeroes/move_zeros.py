
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        llist=[]
        for n in nums:
            if n==0:
                count+=1
            else:
                llist.append(n)
        for n in range(count):
            llist.append(0)
        for n in range(len(llist)):
            nums[n] =llist[n]
            
nums = [0,1,0,3,12]
s = Solution()
s.moveZeroes(nums)
print(nums)