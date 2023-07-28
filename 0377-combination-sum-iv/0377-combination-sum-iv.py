class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo ={}
        
        def dfs(curr_num):
            if curr_num < 0 :
                return 0
            if curr_num == 0:
                return 1
            
            if curr_num in memo:
                return memo[curr_num]
            result = 0
            
            for num in nums:
                result += dfs(curr_num - num)
            
            memo[curr_num] = result
            return result
        
        return dfs(target)