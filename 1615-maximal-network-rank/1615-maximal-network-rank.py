class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjacency_list = defaultdict(set)
        
        for node1, node2 in roads:
            adjacency_list[node1].add(node2)
            adjacency_list[node2].add(node1)
            
        
        result = 0
        
        for node1 in range(n- 1):
            for node2 in range(node1 + 1, n):
                neigh1 = len(adjacency_list[node1])
                neigh2 = len(adjacency_list[node2])
                
                if node2 in  adjacency_list[node1]:
                    result = max(result, neigh1 + neigh2 -1)
                else:
                    result = max(result, neigh1 + neigh2)
        
        return result
        