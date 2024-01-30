class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        pref_sums = [([0] * m) for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                
                if i == 0 and j == 0:
                    pref_sums[i][j] = 0
                
                elif i == 0:
                    pref_sums[i][j] = pref_sums[i][j - 1]
                
                elif j == 0:
                    pref_sums[i][j] = pref_sums[i - 1][j] 
                
                else:
                    pref_sums[i][j] = pref_sums[i - 1][j] + pref_sums[i][j - 1] - pref_sums[i - 1][j -1]
                
                pref_sums[i][j] += matrix[i][j]
            
        res = 0
        for r1 in range(n):
            for r2 in range(r1, n):
                
                diction = defaultdict(int)
                diction[0] = 1
                
                for col in range(m):
                    
                    tot = pref_sums[r2][col]
                    
                    if r1 != 0:
                        tot -= pref_sums[r1 - 1][col]
                    
                    res += diction[tot - target]
                    diction[tot] += 1
        return res