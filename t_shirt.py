def proccess(first, last):
    first_scale = 0
    first_res = 0

    for i in range(len(first)):
    
        if first[i]=="X":
            first_scale +=1
    
        elif first[i]=="M":
            first_res = 1
    
        elif first[i]=="L":
            first_res= 2 + first_scale

        else:
            first_res = 0 - first_scale
    
    second_scale = 0
    second_res = 0

    for j in range(len(last)):
    
        if last[j]=="X":
            second_scale +=1
    
        elif last[j]=="M":
            second_res = 1
    
        elif last[j]=="L":
            second_res= 2 + second_scale

        else:
            second_res = 0 - second_scale

    if first_res > second_res:
        print(">")
    
    elif first_res == second_res:
        print("=")
    
    else:
        print("<")


count = int(input())

for  _ in range(count):
    first, last = input().split()
    proccess(first, last)
