class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        memo = {}
        
        def dp(ind):
            
            if ind >= len(questions):
                return 0
            if ind in memo:
                return memo[ind]
            choice1 = dp(ind + 1)
            choice2 = dp(ind + questions[ind][1] + 1) + questions[ind][0]
            memo[ind] = max(choice1, choice2)
            return max(choice1, choice2)
        
        return dp(0)