class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        colInfo = defaultdict(int)
        rowColumnPairs = 0
        
        for idx in range(len(grid[0])):
            llist =[]
            for idx2 in range(len(grid)):
                llist.append(grid[idx2][idx])
            colInfo[tuple(llist)] += 1
        
        print(colInfo)
        
        for idx in range(len(grid)):
            rowColumnPairs += colInfo[tuple(grid[idx])]
            
        return rowColumnPairs