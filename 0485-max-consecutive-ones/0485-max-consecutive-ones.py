class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        leftPtr = 0
        maxRes = 0
        
        for rightPtr in range(len(nums)):
            if nums[rightPtr] == 1:
                maxRes = max(maxRes, rightPtr - leftPtr + 1)
            else:
                leftPtr = rightPtr + 1
        return maxRes
        