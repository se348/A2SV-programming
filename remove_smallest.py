def process(llist):
    llist.sort()
    elem = llist[0]
    for i in range(1, len(llist)):
        if llist[i] - elem >1:
            print("NO")
            return 
        elem = llist[i]
    print("YES")

test =int(input())

for i in range(test):
    j = input()
    llist = list(map(int, input().split()))
    process(llist)
