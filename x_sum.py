import collections


def process(matrix, rows, cols):
    diff = collections.defaultdict(int)
    add = collections.defaultdict(int)

    for row in range(rows):
        for col in range(cols):
            
            diff[row - col] += matrix[row][col]
            add[ row + col] += matrix[row][col]

    maximal_res = 0

    for row in range(rows):
        for col in range(cols):
            maximal_res= max(maximal_res, diff[row - col] + add[ row + col]- matrix[row][col])

    print(maximal_res)
            




test = int(input())

for i in range(test):
    
    rows, cols = list(map(int,input().split()))
    mat = []
    for j in range(rows):
        temp = list(map(int,input().split()))
        mat.append(temp)
    
    process(mat, rows, cols)
    
