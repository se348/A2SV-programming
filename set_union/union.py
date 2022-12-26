# Enter your code here. Read input from STDIN. Print output to STDOUT# Enter your code here. Read input from STDIN. Print output to STDOUT
set_length  = int(input())
set1 = set(map(int, input().split()))
set2_length  = int(input())
set2 = set(map(int, input().split()))

union = set1.union(set2)
print(len(union))
