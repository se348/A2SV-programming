from typing import List


class Solution:
    result1=-1
    result2=-1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low =0
        high= len(nums)-1
        while low<=high:
            mid= (low+ high)//2
            if nums[mid] == target:
                self.search(nums, target, low, mid, True)
                self.search(nums, target, mid, high, False)
                break
            elif nums[mid]< target:
                low =mid+1
            else:
                high= mid-1
        return [self.result1, self.result2]
        
    def search(self,nums, target,low, high, isFirst):
        while low<=high:
            mid= (low+ high)//2
            if nums[mid] == target:
                if isFirst:
                    self.result1= mid
                    high= mid-1
                else:
                    self.result2= mid
                    low= mid+1
            elif nums[mid]< target:
                low =mid+1
            else:
                high= mid-1
