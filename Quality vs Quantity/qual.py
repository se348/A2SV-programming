def solve(length,llist):
    llist.sort()
    l, r = 1, length-1
    large_sum = llist[0]
    small_sum = 0
    while l < r:
        large_sum += llist[l]
        small_sum += llist[r]
        l +=1
        r -=1
        if small_sum > large_sum:
            print('YES')
            return

    print('NO')

t= int(input())
for _ in range(t):
    length =int(input())
    inputta =input().split()
    llist = list(map(int,inputta))
    solve(length, llist)

#solve(10,[9,10,2,3,4,8,10,17])
    