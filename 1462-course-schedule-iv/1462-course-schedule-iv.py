class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        mat = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        
        for src, dest in prerequisites:
            mat[src][dest] = True
        
        
        for k in range(numCourses):
            
            for i in range(numCourses):
                for j in range(numCourses):
                    
                    if mat[i][j]:
                        continue
                    
                    mat[i][j] = mat[i][k] and mat[k][j]
        
        result = []
        
        for i, j in queries:
            result.append(mat[i][j])
        
        return result