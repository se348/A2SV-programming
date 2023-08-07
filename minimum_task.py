from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]):
        # code here
        inwards = [0] * n
        adjacencyList = defaultdict(list)
        
        for i,j in edges:
            inwards[j - 1] += 1
            adjacencyList[i - 1].append(j - 1)
        
        visited = set()
        queue = deque()
        
        for i in range(n):
            if inwards[i] == 0:
                queue.append(i)
                visited.add(i)
        result =[0] * n
        count = 0
        while queue:
            count += 1
            
            for i in range(len(queue)):
                prev = queue.popleft()
                result[prev] =  count
                for j in adjacencyList[prev]:
                    inwards[j] -= 1
                    if j not in visited and inwards[j] == 0:
                        queue.append(j)
                        visited.add(j)
        return result
