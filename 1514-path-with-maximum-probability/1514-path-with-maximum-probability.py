class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        
        adjacency_list = defaultdict(list)
        
        for i in range(len(edges)):
            n1, n2 = edges[i]
            adjacency_list[n1].append((n2, succProb[i]))
            adjacency_list[n2].append((n1, succProb[i]))
            
        
        max_heap = [(-1, start)]
        distance = defaultdict(int)
        
        while max_heap:
            curr_distance, curr_node = heapq.heappop(max_heap)
            curr_distance *= -1
            
            if curr_distance < distance[curr_node]:
                continue
            
            if curr_node == end:
                return curr_distance
            
            distance[curr_node] = curr_distance
            for neighbor_n, neighbor_w in adjacency_list[curr_node]:
                if (curr_distance * neighbor_w) > distance[neighbor_n]:
                    distance[neighbor_n] = (curr_distance * neighbor_w)
                    heapq.heappush(max_heap, (-(curr_distance * neighbor_w), neighbor_n))
        return 0