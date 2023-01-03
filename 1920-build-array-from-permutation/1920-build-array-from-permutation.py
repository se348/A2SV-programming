class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new_arr= [0 for i in range(len(nums))]
        
        for j in range(len(nums)):
            new_arr[j] = nums[nums[j]]
            
        return new_arr