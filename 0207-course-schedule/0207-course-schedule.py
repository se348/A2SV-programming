class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        unvisited = 0
        openend = 1
        closed = 2
        
        arr = [unvisited for i in range(numCourses)]
        adjacency_list = collections.defaultdict(list)
        
        def dfs(course):
            arr[course] = openend
            for next_course in adjacency_list[course]:
                if arr[next_course] == openend:
                    return False
                elif arr[next_course] == unvisited:
                    if not dfs(next_course):
                        return False
            
            arr[course] = closed
            return True
        
        for i, j in prerequisites:
            adjacency_list[j].append(i)
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
            
        
                
        
        
        