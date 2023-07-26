class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(ind):
            if ind >= len(cost):
                return 0
            if ind in memo:
                return memo[ind]

            curr = cost[ind]
            
            temp = min(dfs(ind + 1), dfs(ind + 2))
            memo[ind]= temp + curr
            return memo[ind]
        return min(dfs(0), dfs(1))