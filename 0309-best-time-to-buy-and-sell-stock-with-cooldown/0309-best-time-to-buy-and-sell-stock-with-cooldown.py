class Solution:
    def __init__(self):
        self.memo={}
    def dfs(self, index, own, prices):    
        if index>=len(prices):
            return 0
        if (index, own) in self.memo:
            return self.memo[(index, own)]
        if own:
            choice1 = self.dfs(index + 2, False, prices)
            choice2 = self.dfs(index + 1, True, prices)
            self.memo[(index, own)] = max(choice1 + prices[index] , choice2)
            return self.memo[(index, own)]
        
        choice1 = self.dfs(index + 1, True, prices)
        choice2 = self.dfs(index + 1, False, prices)
        self.memo[(index, own)] = max(choice1 - prices[index] , choice2)
        return self.memo[(index, own)]
        
        
    def maxProfit(self, prices: List[int]) -> int:
        return self.dfs(0, False, prices)