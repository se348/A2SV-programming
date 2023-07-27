class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(currSum, ind):
            if ind == len(nums):
                if currSum == 0:
                    return 1
                return 0
            
            opt1 = currSum + nums[ind]
            opt2 = currSum - nums[ind]
            
            ans_opt1, ans_opt2 = 0,0
            
            if (opt1, ind + 1) in memo:
                ans_opt1 = memo[(opt1, ind + 1)]
            else:
                ans_opt1 = dp(opt1, ind + 1)
                memo[(opt1, ind + 1)] = ans_opt1
                
            if (opt2, ind + 1) in memo:
                ans_opt2 = memo[(opt2, ind + 1)]
            else:
                ans_opt2 = dp(opt2, ind + 1)
                memo[(opt2, ind + 1)] = ans_opt2
                
            return ans_opt1 + ans_opt2
        
        return dp(target, 0)