class Solution:
    
    def constructGraph(self, nums):
        graph = defaultdict(list)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                
                euclid = math.sqrt((nums[i][1] - nums[j][1])**2 + (nums[i][0] - nums[j][0]) ** 2)
                
                if euclid <=  nums[i][2]:
                    graph[i].append(j)
                    
                if euclid <= nums[j][2]:
                    graph[j].append(i)
                    
        return graph
    
    def maximumDetonation(self, nums: List[List[int]]) -> int:
        
        graph = self.constructGraph(nums)
        res = 1
        for i in range(len(nums)):
            
            curr = graph[i]
            visited = {i}
            q = collections.deque()
            q.append(i)
            count = 0
            if curr:
              
                while q:
                    
                    curr = q.popleft()
                    count+=1
                    res =max(res, count)
                    for j in graph[curr]:
                        if j not in visited:
                            visited.add(j)
                            q.append(j)
        
        return res