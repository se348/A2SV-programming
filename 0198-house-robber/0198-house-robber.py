class Solution:
    def rob(self, nums: List[int]) -> int:
        memo ={}
        
        def dp(ind):
            if ind >= len(nums):
                return 0
            if ind in memo:
                return memo[ind]
            count = nums[ind]
            
            choice1 = dp(ind +1)
            
            choice2 = dp(ind + 2) + count
            
            memo[ind] = max(choice1, choice2) 
            return memo[ind]
        
        return dp(0)