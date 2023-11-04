class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.matrix = [[inf for i in range(n)] for i in range(n)]
        self.n = n
        for i in range(n):
            self.matrix[i][i] = 0
            
        for i, j, e in edges:
            self.matrix[i][j] = e
        
        for k in range(n):
            self.reiterate(k)
        
    def reiterate(self, k):
        
        for i in range(self.n):
            for j in range(self.n):
                self.matrix[i][j] = min(self.matrix[i][j], self.matrix[i][k] + self.matrix[k][j])
        

    def addEdge(self, edge: List[int]) -> None:
        i, j, e = edge
        
        if e < self.matrix[i][j]:
            self.matrix[i][j] = e
            self.reiterate(i)
            self.reiterate(j)

    def shortestPath(self, node1: int, node2: int) -> int:
        path = self.matrix[node1][node2]
        
        return path if path != inf else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)