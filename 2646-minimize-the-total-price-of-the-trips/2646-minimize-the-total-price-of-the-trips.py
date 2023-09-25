class Solution:
        
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        contributions= [0] * n
        adjacency_list= defaultdict(list)
        
        for n1, n2 in edges:
            adjacency_list[n1].append(n2)
            adjacency_list[n2].append(n1)
        
        def dfs(prev, curr_node, target):
            if target == curr_node:
                return 1
            
            for neighbor in adjacency_list[curr_node]:
                if neighbor != prev:
                    if dfs(curr_node, neighbor, target):
                        contributions[neighbor] += 1
                        return 1
            return 0
        
        for n1, n2 in trips:
            contributions[n1] += 1
            dfs(-1, n1, n2)
        
        @cache
        def dp(parent, ind, par_halfed):
            if par_halfed:
                count = 0
                for neighbor in adjacency_list[ind]:
                    if neighbor != parent:
                        count += dp(ind, neighbor, False)
                
                count += (contributions[ind] * price[ind])
                return count
            else:
                count1 = 0
                count2 = 0
                for neighbor in adjacency_list[ind]:
                    if neighbor != parent:
                        count1 += dp(ind, neighbor, False)
                        count2 += dp(ind, neighbor, True)

                count1 += (contributions[ind] * price[ind])
                count2 += (contributions[ind] * price[ind] // 2)
                return min(count1, count2)
        
        return dp(-1, 0, False)
        
