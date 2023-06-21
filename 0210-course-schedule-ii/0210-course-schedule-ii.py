class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencyList = defaultdict(list)
        dependency = defaultdict(int)
        
        for course, prev in prerequisites:
            adjacencyList[prev].append(course)
            dependency[course] += 1
        
        queue =deque()
        
        for i in range(numCourses):
            if dependency[i] == 0:
                queue.append(i)
            
        res = []
        
        while queue:
            curr = queue.popleft()    
            res.append(curr)
            
            for neighbor in adjacencyList[curr]:
                dependency[neighbor] -= 1
                if dependency[neighbor] == 0:
                    queue.append(neighbor)
        
        return res if len(res) == numCourses else []