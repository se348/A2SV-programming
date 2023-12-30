class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        
        @cache
        def dp(ind, remain_d):
            
            if ind == len(jobDifficulty):
                return inf if remain_d != 0 else 0
            
            if not remain_d:
                return inf
            
            curr_max = 0
            res = inf
            
            for i in range(ind + 1, len(jobDifficulty) + 1):
                temp = dp(i, remain_d - 1)
                curr_max = max(curr_max, jobDifficulty[i - 1])
                res = min(res, curr_max + temp)
            
            return res
        
        res = dp(0, d)
        
        return res if res != inf else -1
        