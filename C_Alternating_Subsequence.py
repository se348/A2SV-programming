def process(arr):
    negative  = 0
    positive = 0

    alternate = []

    for num in arr:

        if num > 0: 
        
            if negative == 0:
                positive =max(positive, num)
            else:
                alternate.append(negative)
                negative = 0
                positive = num
        
        else:
            if positive == 0:
                negative =max(negative, num)
                if negative == 0:
                    negative = num
            else:
                alternate.append(positive)
                positive = 0
                negative = num

    if negative != 0:
        alternate.append(negative)
    
    if positive != 0:
        alternate.append(positive)
        
    print(sum(alternate))

testcases = int(input())

for i in range(testcases):
    input()
    arr = list(map(int, input().split()))
    process(arr)
