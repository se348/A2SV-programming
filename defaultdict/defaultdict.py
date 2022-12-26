# Enter your code here. Read input from STDIN. Print output to STDOUTm
from collections import defaultdict

n,m =input().split()

A = defaultdict(list)
for index in range(int(n)):A[input()
    A[input()].append(str(index+1))

for _ in range(int(m)):
    inp = input()
    res= A[inp]
    if not res:
        print(-1)
    else:
        print(" ".join(res))
    
