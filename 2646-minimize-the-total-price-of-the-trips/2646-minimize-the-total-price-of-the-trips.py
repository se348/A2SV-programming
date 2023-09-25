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
        
#         def dp(par, ind, halfed):
            
#             if (ind, halfed) in memo:
#                 return memo[(ind, halfed)]
            
#             curr1, curr2 = 0, 0
#             for neighbor in adjacency_list[ind]:
#                 if neighbor != par:
#                     if halfed:
#                         curr1 += dp(ind, neighbor, False) 
#                     else:
#                         curr1 += dp(ind, neighbor, False)
#                         curr2 += dp(ind, neighbor, True) 
                        
#             res = 0
#             if halfed:
#                 res = curr1 + (contributions[ind] * (price[ind] // 2))
#             else:
#                 res = min(curr1, curr2) + (contributions[ind] * price[ind])
                
            
#             memo[(ind, halfed)] = res
#             return res
        
#         res1 = dp(-1, 4, True)
#         res2 = dp(-1, 4, False)
        @cache
        def dp(node, parent, halve):


            res1 = inf
            if not halve:
                res1 = price[node] // 2 * contributions[node]
                for nei in adjacency_list[node]:
                    if nei != parent:
                        res1 += dp(nei, node, not halve)

            res2 = price[node] * contributions[node]
            for nei in adjacency_list[node]:
                if nei != parent:
                    res2 += dp(nei, node, False)
            return min(res1, res2)
        return dp(0, -1, False )
