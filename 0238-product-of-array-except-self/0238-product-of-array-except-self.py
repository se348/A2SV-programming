class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [ 1 ] * ( len(nums) + 1)
        suffix = [ 1 ] * ( len(nums) + 1)
        
        for ind in range(len(nums)):
            prefix[ind + 1] = prefix[ind] * nums[ind]
        for ind in range(len(nums)-1, -1, -1):
            suffix[ind] = suffix[ind + 1] * nums[ind]
        
        res = [1] * len(nums)
        for ind in range(len(nums)):
            res[ind] = prefix[ind] * suffix[ind + 1]
        
        return res