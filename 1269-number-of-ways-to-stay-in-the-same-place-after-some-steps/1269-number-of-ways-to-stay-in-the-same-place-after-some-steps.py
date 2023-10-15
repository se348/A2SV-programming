class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(arrLen, steps)
        
        
        @cache
        def dp(remaining_step, curr_ind):
            if curr_ind < 0 or curr_ind >= (arrLen):
                return 0
            if remaining_step == 0 and curr_ind != 0:
                return 0
            if remaining_step == 0:
                return 1
            
            a = dp(remaining_step - 1, curr_ind - 1)
            b = dp(remaining_step - 1, curr_ind)
            c = dp(remaining_step - 1, curr_ind + 1)
            
            return (a + b+ c) % ((10 ** 9) + 7)
        
        return dp(steps, 0)
        