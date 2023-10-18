class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * n
        adjacency_list = [[] for i in range(n)]
        
        for c1, c2  in relations:
            adjacency_list[c1 - 1].append(c2 - 1)
            indegree[c2 - 1] += 1
        
        curr_time = 0
        
        queue = deque()
        
        new_time = time.copy()        
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append((i,  time[i]))
                
        
        while queue:
            curr_node, curr_time = queue.popleft()
            
            for neighbor in adjacency_list[curr_node]:
                indegree[neighbor] -= 1
                new_time[neighbor] = max(time[neighbor] + curr_time, new_time[neighbor])
                
                if indegree[neighbor] == 0:
                    queue.append((neighbor, new_time[neighbor]))
        
        return max(new_time)