class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        totalCosts = 0
        
        for i, cost in enumerate(costs):
            
            if totalCosts + cost <= coins:
                totalCosts += cost
            else:
                return i
            
        return len(costs)
        