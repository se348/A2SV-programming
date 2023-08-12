class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        tot = (2** m) - 1
        
        mat = []
        for i in range(n):
            curr_sum = 0
            k= 1
            for j in range(m -1, -1, -1):
                if grid[i][j]:
                    curr_sum += k
                k *= 2
                
            mat.append(curr_sum)
        
        for i in range(n):
            mat[i] = max(mat[i], tot - mat[i])
        
        res = sum(mat)
        for i in range(m):
            count = 0
            
            for j in range(n):
                if mat[j] & pow(2, i):
                    count += 1
            if n - count > count:
                curr = (n - (2* count))
                res += (pow(2, i) * curr)
        return res
            
        return 0