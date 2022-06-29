class Solution:
    def maxFrequency(self, nums: list, k: int) -> int:
        nums.sort()
        left, right =0, 0
        res, total =0, 0
        while right< len(nums):
            total +=nums[right]

            while nums[right] * (right - left + 1) > total + k:
                total -=nums[left]
                left += 1
            res =max(res, right-left +1)
            right+= 1
        return res

s= Solution()
a =s.maxFrequency( [3,9,6], 2)
print(a)