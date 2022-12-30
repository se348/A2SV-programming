
def proccess(length, llist, stringo):
    diction ={}
    for  i in range(length):
        if llist[i] in diction and stringo[i]== diction[llist[i]]:
            continue
        elif llist[i] not in diction:
            diction[llist[i]] = stringo[i]
        else:
            print("NO")
            return
    print("YES")

test_cases = int(input())
for _ in range(test_cases):
    length = input()
    llist = input().split()
    stringo = input()
    proccess(int(length),llist, stringo)
