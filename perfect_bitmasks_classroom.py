t = int(input())

def calculate(x):

    first_one = -1
    second_one = -1

    bit = 1

    while bit <= x:
        if bit & x:
            if first_one == -1:
                first_one = bit
            elif second_one == -1:
                second_one = bit
                break
        bit <<= 1
    if second_one != -1:
        print(first_one)
        return
    
    bit = 1
    while True:
        if not(bit & x):
            print(first_one + bit)
            return
        bit <<= 1

for _ in range(t):
    x = int(input())
    calculate(x)
