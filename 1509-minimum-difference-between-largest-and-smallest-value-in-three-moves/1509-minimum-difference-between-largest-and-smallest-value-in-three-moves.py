class Solution:
    def minDifference(self, nums: List[int]) -> int:
        length = len(nums)
        
        nums.sort()
        
        if length <= 4:
            return 0
        
        option1 = nums[length - 1] - nums[3]
        option2 = nums[length - 4] - nums[0]
        
        option3 = nums[length - 2] - nums[2]
        option4 = nums[length - 3] - nums[1]
        
        return min(option1, option2, option3, option4)