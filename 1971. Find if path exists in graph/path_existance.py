import collections
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        stck = [source]
        visited = {source}
        while stck:
            curr = stck.pop()
            if curr == destination:
                return True
            for i in graph[curr]:
                if i not in visited:
                    stck.append(i)
                    visited.add(i)
        return False