def proccess(arr1, arr2, size_1, size_2):
    lft_ptr , rght_ptr = 0, 0
    res = []
    
    while lft_ptr < size_1 or rght_ptr < size_2:
        
        if rght_ptr == size_2 or (lft_ptr < size_1 and arr1[lft_ptr] < arr2[rght_ptr]):
            
            res.append(arr1[lft_ptr])
            lft_ptr += 1        
            
        else:
            res.append(arr2[rght_ptr])
            rght_ptr += 1
    print(*res)

size_1 , size_2 = list(map(int, (input().split())))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

proccess(arr1, arr2, size_1, size_2)
