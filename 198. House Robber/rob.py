from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def dfs(index):
            if index in memo:
                return memo[index]
            if index>=len(nums):
                return 0
            a=dfs(index+1)
            b= dfs(index+2) + nums[index]
            memo[index] = max(a,b)
            return max(a,b)
        return dfs(0)
            
        