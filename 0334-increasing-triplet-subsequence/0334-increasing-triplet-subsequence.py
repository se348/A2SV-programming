class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1, num2 = math.inf, math.inf

        for num in nums:
            if num < num1:
                num1 = num
            elif num1 < num < num2:
                num2 = num
            elif  num2 < num:
                return True

        return False