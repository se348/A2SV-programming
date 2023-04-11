class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        
        accumulate = 0
        result = []
        
        for i in range(len(nums)):
            accumulate += nums[i]
            greaterThan = total - accumulate
            option1 = (nums[i] * (i + 1)) - accumulate
            option2 = greaterThan - (nums[i] * (len(nums) - i -1))
            result.append(option1 + option2)
            
        return result