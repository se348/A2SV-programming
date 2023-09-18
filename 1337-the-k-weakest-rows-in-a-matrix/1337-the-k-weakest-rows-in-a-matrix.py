class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = []
        length = len(mat)
        
        for i in range(length):
            soliders = sum(mat[i])
            result.append((soliders, i))
            
        result.sort()
        return [result[i][1] for i in range(k)]
            
        