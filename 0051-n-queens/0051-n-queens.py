class Solution:
    def constructPath(self,path, n):
        result = [["." for j in range(n)] for i in range(n)]
        for i, j in path:
            result[i][j] = "Q"
            
        for i in range(n):
            result[i]= "".join(result[i])
            
        return result
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        visited_row = set()
        visited_col = set()
        visited_diag = set()
        reverse_diag = set()
        
        ans = []
        def dfs(i, j, path):
            if i == n or j ==n:
                ans.append(self.constructPath(path, n))
                return True
            if i in visited_row:
                return False
            if j in visited_col:
                return False
            if j -i in visited_diag:
                return False
            if i + j in reverse_diag:
                return False
            
            visited_row.add(i)
            visited_col.add(j)
            visited_diag.add(j - i)
            reverse_diag.add(i + j)
            
            path.append((i,j))
            
            for k in range(n):
                
                temp = dfs(i + 1, k, path)
                if temp:
                    break
            path.pop()
            
            visited_row.remove(i)
            visited_col.remove(j)
            visited_diag.remove(j - i)
            reverse_diag.remove(i + j)
        
        path= []
        for i in range(n):
            dfs(0, i, path)
        return ans