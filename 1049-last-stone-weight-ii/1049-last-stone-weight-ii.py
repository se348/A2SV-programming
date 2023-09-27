class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) / 2
        
        closest = inf
        
        @cache
        def dp(ind, curr_sum):
            nonlocal closest
            if ind == len(stones):
                if abs(target - curr_sum) < abs(closest - target):
                    closest = curr_sum
                return
            
            dp(ind + 1, curr_sum + stones[ind])
            dp(ind + 1, curr_sum)
        
        dp(0, 0)
        
        return int(abs(closest - target) * 2)