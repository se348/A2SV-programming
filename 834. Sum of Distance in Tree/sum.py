from collections import defaultdict
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adjacency_list = defaultdict(list)
        for x,y in edges:
            adjacency_list[x].append(y)
            adjacency_list[y].append(x)
        
        helperCount= [0] *n
        visited= {0}
        soln=[0]*n
        def dfs(curr):
            count =1
            for child in adjacency_list[curr]:
                if child in visited:
                    continue
                visited.add(child)
                tempo=dfs(child)
                count+=tempo
                soln[0]+=tempo
            helperCount[curr] = count
            return count
        
        dfs(0)
        visited={0}
        def dfs2(curr):
            for child in adjacency_list[curr]:
                if child not in visited:
                    visited.add(child)
                    soln[child]= soln[curr]- helperCount[child] + (n- helperCount[child])
                    dfs2(child)
        dfs2(0)
        return soln
        
        