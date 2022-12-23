# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split())

N= int(input())
cond= True
for _ in range(N):
    otherSet = set(input().split())
    if not a.issuperset(otherSet):
        cond=False
        break
if cond:
    print(True)
else: print(False)