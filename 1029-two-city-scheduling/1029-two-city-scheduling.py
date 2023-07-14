class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        for i in range(len(costs)):
            costs[i].append(costs[i][0] - costs[i][1])
        
        costs.sort(key= lambda i: i[2])
        
        result = 0
        for i in range(len(costs)//2):
            result += costs[i][0]
        
        for j in range(len(costs)//2, len(costs)):
            result += costs[j][1]
        return result