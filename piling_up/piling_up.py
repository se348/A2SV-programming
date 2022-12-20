# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import inf
test_cases = int(input())

for _ in range(test_cases):
    length = int(input())
    blocks = input().split()
    i = 0
    j= length- 1
    flag= False
    highest = inf
    while i<=j:
        left = int(blocks[i])
        right = int(blocks[j])
        if left<= highest and left>=right:
            i+=1
            highest=left
        elif right<=highest:
            j-=1
            highest=right
        else:
            flag=True
            break
    if flag:
        print("No")
    else:print("Yes")
