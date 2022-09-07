class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        visited_index= {}
        def dfs(curr_pos):
            if curr_pos in visited_index:
                return visited_index[curr_pos]
            if curr_pos>=len(cost):
                return 0
            first= dfs(curr_pos+1)
            second= dfs(curr_pos+2)
            visited_index[curr_pos] =cost[curr_pos]+ min(first, second)
            return visited_index[curr_pos]
            
        ans = min(dfs(0), dfs(1))
        return ans