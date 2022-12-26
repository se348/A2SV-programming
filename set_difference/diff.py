# Enter your code here. Read input from STDIN. Print output to STDOUT
english_length  = int(input())
english = set(map(int, input().split()))
french_length  = int(input())
french = set(map(int, input().split()))

diff = english.difference(french)
print(len(diff))
