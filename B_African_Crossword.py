from collections import defaultdict

def proccess(grid, rows:int, cols:int):
    row_dicts = [defaultdict(list) for i in range(rows)]
    col_dicts = [defaultdict(list) for i in range(cols)]
    
    for row in range(rows):
        for col in range(cols):
            curr_val = grid[row][col]
            col_dicts[col][curr_val].append(row)
            row_dicts[row][curr_val].append(col)
    
    res= []

    for row in range(rows):
        for col in range(cols):
            curr_val = grid[row][col]
            
            if len(row_dicts[row][curr_val]) != 1 or len(col_dicts[col][curr_val]) != 1:
                continue
            else:
                res.append(curr_val[0])
                
    print("".join(res))
    
            


rows, cols = list(map(int,input().split()))
grid = []
for _ in range(rows):
    grid.append(input())
    
proccess(grid, rows, cols)
