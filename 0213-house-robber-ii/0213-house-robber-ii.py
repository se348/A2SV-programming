class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(ind, maxim_ind, memo):
            if ind >= maxim_ind:
                return 0
            if ind in memo:
                return memo[ind]
            choice1 = dp(ind +1, maxim_ind, memo)
            choice2 = dp(ind+ 2, maxim_ind, memo) + nums[ind]
            result = max(choice1, choice2)
            memo[ind] = result
            return result
        n=len(nums)
        if n == 1:
            return nums[0]
        memo = {}
        choice1= dp(0,n - 1, memo)
        memo = {}
        choice2 = dp(1, n, memo)
        return max(choice1, choice2)
        