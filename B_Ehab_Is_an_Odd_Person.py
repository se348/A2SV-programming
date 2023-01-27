test = int(input())

arr = list(map(int, input().split()))
isEven = False
isOdd = False

for num in arr:
    if num % 2 == 0:
        isEven = True
    else:
        isOdd = True

    if isEven and isOdd:
        break

if isEven and isOdd:
    arr.sort()
    print(*arr)

else:
    print(*arr)
