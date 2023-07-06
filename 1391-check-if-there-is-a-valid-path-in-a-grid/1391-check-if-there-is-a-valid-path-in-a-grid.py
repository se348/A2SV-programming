class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        parent=defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                parent[(i,j)]=(i,j)
                
        
        rank=[[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        
        def inbound(row,col):
            return 0<=row<=len(grid)-1 and 0<=col<=len(grid[0])-1
        
        def find( x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(pair1,pair2):
            parentX=find(pair1)
            parentY=find(pair2)
            if parentX == parentY:
                return
            elif rank[parentX[0]][parentX[1]] == rank[parentY[0]][parentY[1]]:
                rank[parentX[0]][parentX[1]] += 1
            if rank[parentX[0]][parentX[1]] > rank[parentY[0]][parentY[1]]:
                parent[parentY]=parentX
            else:
                parent[parentX]=parentY
       

        
        right = {1: {1, 3, 5}, 2: {}, 3: {}, 4: {1, 3, 5}, 5: {}, 6: {1, 3, 5}}
        down = {1: {}, 2: {2, 5, 6}, 3: {2, 5, 6}, 4: {2, 5, 6}, 5: {}, 6: {}}
        
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                    if inbound(row, col + 1)and  grid[row][col + 1] in right[grid[row][col]]:
                        
                        union((row,col),(row, col + 1))
                    if inbound(row + 1, col)and  grid[row + 1][col] in down[grid[row][col]]:
                        union((row + 1,col),(row,col))
        
        return find((0,0)) == find((len(grid) - 1, len(grid[0]) - 1))
                
        
        