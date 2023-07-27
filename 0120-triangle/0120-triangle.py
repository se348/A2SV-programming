class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        
        def dfs(row, col):
            if row >= len(triangle):
                return 0
            
            if col >= len(triangle[row]):
                return inf
            if (row, col) in memo:
                return memo[(row, col)]
            
            option1 = dfs(row + 1, col)
            option2 = dfs(row + 1, col + 1)
            
            ans = min(option1, option2) + triangle[row][col]
            memo[(row, col)] = ans
            return ans
        
        return dfs(0,0)
        