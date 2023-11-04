class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        mat = []
        
        adjacency_list = {}
        for n1, n2, e in edges:
            adjacency_list[(n1, n2)] = e
            adjacency_list[(n2, n1)] = e
        
        for i in range(n):
            arr = []
            
            for j in range(n):
                if (i == j):
                    arr.append(0)
                elif (i, j) in adjacency_list:
                    arr.append(adjacency_list[(i, j)])
                else:
                    arr.append(inf)
            
            mat.append(arr)
            
        for k in range(n):
            
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
        
        node = -1
        value = inf
        
        for i in range(n):
            curr_count = 0
            
            for j in range(n):
                if mat[i][j] <= distanceThreshold:
                    curr_count += 1
            
            if curr_count <= value:
                node = i
                value = curr_count
        return node
                
        return 0
            