# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = input()
arr = input().split()
a =set(input().split())
b= set(input().split())
happiness = 0
for i in arr:
    if i in a:
        happiness+=1
    elif i in b:
        happiness-=1
print(happiness)
