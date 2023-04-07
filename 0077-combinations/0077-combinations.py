class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        arrs = []
        
        def backtrack(path):
            if len(path) == k:
                arrs.append(path[:])
                return
            
            minimum = 0
            
            if path:
                minimum = path[-1]
            
            for i in range(minimum +1, n+1):
                path.append(i)
                backtrack(path)
                path.pop()
        
        backtrack([])
        return arrs