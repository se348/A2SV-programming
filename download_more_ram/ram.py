test =int(input())
for _ in range(test):
    curr_ram = str(input()).split()
    curr_ram= int(curr_ram[1])
    a= input().split()
    a= list(map(int, a))
    b= input().split()
    for i in range(len(b)):
        a[i] =(a[i], int(b[i]))
    res= sorted(a)
    cond= False
    for need,benefit in res:
        if need> curr_ram:
            print(curr_ram)
            cond=True
            break
        curr_ram+=benefit
    if cond==False:    
        print(curr_ram)