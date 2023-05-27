class Solution:
    def minJumps(self, arr: List[int]) -> int:
        indexes = defaultdict(list)
        
        for i in range(len(arr) -1, -1, -1):
            indexes[arr[i]].append(i)
        
        queue = deque()
        queue.append((0, 0))
        visited = {0}
        
        k = 0 
        while queue:
            curr, step = queue.popleft()          
            if curr == len(arr) -1:
                return step
            
            if curr < len(arr) - 1 and curr + 1 not in visited:
                visited.add(curr + 1)
                queue.append((curr + 1, step + 1))
                
            if curr >= 1 and curr - 1 not in visited:
                visited.add(curr - 1)
                queue.append((curr - 1, step + 1))
            
            for j in indexes[arr[curr]]:
                if j not in visited:
                    visited.add(j)
                    queue.append((j, step + 1))
                    
            indexes[arr[curr]].clear()

        