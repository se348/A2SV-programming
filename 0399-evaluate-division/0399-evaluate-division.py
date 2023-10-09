class Solution:
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        temp = {}
        length = len(equations)
        
        for i in range(length):
            a, b = equations[i]
            
            if a not in temp:
                temp[a] = len(temp)
            if b not in temp:
                temp[b] = len(temp)
        
        mat = [[-1 for i in range(len(temp))] for j in range(len(temp))]
        
        for i in range(length):
            a, b = equations[i]
            mat[temp[a]][temp[b]] = values[i]
            mat[temp[b]][temp[a]] = (1 / values[i])
        
        temp_length = len(temp)
        
        for k in range(temp_length):
            
            for i in range(temp_length):
                for j in range(temp_length):
                    
                    if i!=j and i!=k and mat[i][k] != -1 and mat[k][j] != -1:
                        mat[i][j] = mat[i][k] * mat[k][j]
        
        res= []
        
        for i, j in queries:
            
            if i not in temp or j not in temp:
                res.append(-1)
            elif i == j:
                res.append(1)
            else:                
                res.append(mat[temp[i]][temp[j]])    
        
        return res
        
       