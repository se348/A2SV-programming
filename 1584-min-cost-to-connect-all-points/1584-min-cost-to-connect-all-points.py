class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        
        cost = 0
        
        min_heap = [(0,0)]
        
        while min_heap and len(visited) < len(points):
            curr_cost, curr_ind = heapq.heappop(min_heap)
            if curr_ind in visited:
                continue
            visited.add(curr_ind)
            cost += curr_cost
            
            for i in range(len(points)):
                if i not in visited:
                    p = points[curr_ind]
                    q = points[i]
                    heapq.heappush(min_heap, (abs(p[0] - q[0]) + abs(p[1] - q[1]), i))
        return cost
            