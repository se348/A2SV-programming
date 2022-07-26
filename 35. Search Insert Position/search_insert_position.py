from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.helpermethod(nums, 0, len(nums)-1, target)
    def helpermethod(self, nums, start, end, target):
        if start ==0 and nums[start]> target:
            return 0
        if nums[end]< target:
            return end+1 
        if nums[start]> target:
            return start-1
        if end -start ==1 and target> nums[start] and target<nums[end]:
            return end
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        if nums[(start+end)//2] == target:
            return (start+end)//2
        elif nums[(start+end)//2] < target:
            return self.helpermethod(nums, (start+end)//2, end, target)
        elif nums[(start+end)//2] > target:
            return self.helpermethod(nums, start, (start+end)//2, target)
            

s= Solution()
a =s.searchInsert([1,3], 3)
print(a)