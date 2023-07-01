class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_graph = defaultdict(list)
        col_graph = defaultdict(list)
        
        row_result = [-1] * ( k + 1)
        col_result = [-1] * ( k + 1)
        
        for above, below in rowConditions:
            row_graph[above].append(below)
            
        for left, right in colConditions:
            col_graph[left].append(right)
        
        curr = [k, k]
        
        def dfs(ind,li, graph, typ):
            li[ind] = -2
            
            for i in graph[ind]:
                
                if li[i] == -2:
                    return False
                
                if li[i] == -1:
                    if not dfs(i, li, graph, typ):
                        return False                
            
            li[ind] = curr[typ]
            curr[typ] -= 1
            
            return True
        
        for i in range(1, k + 1):
            if row_result[i] == -1:
                if not dfs(i, row_result, row_graph, 0):
                    return []
        
        for i in range(1, k + 1):
            if col_result[i] == -1:
                if not dfs(i, col_result, col_graph, 1):
                    return []
                
       
        
        result = [[0 for _ in range(k)] for _ in range(k)]
        
        for i in range(1, k + 1):
            r = row_result[i]
            c = col_result[i]
            result[r - 1][c - 1] = i    
        
        return result
                        