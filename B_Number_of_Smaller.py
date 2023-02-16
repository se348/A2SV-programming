def slide(arr1, size_left, arr2, size_right):
    l = 0
    res =[]
 
    for r in range(size_right):
 
        while l < size_left - 1 and arr1[l+1] < arr2[r]:
            l += 1
            first_check = True
        if l==0 and arr1[l] >= arr2[r]:
            res.append(0)
        else:
            res.append(l+1)
    
    print(*res)
 
size_left , size_right = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int, input().split()))
 
slide(arr1, size_left, arr2, size_right)
