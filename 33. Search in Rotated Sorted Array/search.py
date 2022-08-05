from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low= 0
        high= len(nums) - 1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<= nums[high]:
                if nums[high] >= target and target> nums[mid]:
                    low= mid+1
                else: high=mid-1
            else:
                if nums[low] <= target and target<nums[mid] :
                    high=mid-1
                else:
                    low =mid+1
        return -1
                