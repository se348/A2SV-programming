from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        max_count = 0
        while right < len(nums):
            if nums[right] == 1:
                right += 1
            elif nums[right] == 0 and k > 0:
                k -= 1
                right += 1
            else:
                if nums[left] == 0:
                    k += 1
                left += 1
            if right-left > max_count:
                max_count = right -left

        return max_count

    
s= Solution()
s.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2)