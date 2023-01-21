class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num1 = -1
        count = 0
        for num in nums:
            if num == num1:
                count += 1
            elif count == 0:
                num1 = num
                count = 1
            else:
                count -= 1
        return num1