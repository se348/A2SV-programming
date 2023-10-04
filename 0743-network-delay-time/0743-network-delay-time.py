class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency_list = defaultdict(list)
        
        for u, v, w in times:
            adjacency_list[u].append((v, w))
        
        distance_list = defaultdict(lambda: inf)
        min_heap = [(0, k)]
        
        distance_list[k] = 0
        
        while min_heap:
            curr_distance, curr_node = heapq.heappop(min_heap)
            
            if distance_list[curr_node] < curr_distance:
                continue
            
            for neighbor_node, neighbor_weight in adjacency_list[curr_node]:
                if (neighbor_weight + curr_distance) < distance_list[neighbor_node]:
                    heapq.heappush(min_heap, (neighbor_weight + curr_distance, neighbor_node))
                    distance_list[neighbor_node] = (neighbor_weight + curr_distance)
        
        result = -1
        
        for i in range(1, n + 1):
            if distance_list[i] == inf:
                return -1
            
            result = max(result, distance_list[i])
                
        
        return result