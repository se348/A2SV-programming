# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
count = int(input())
words= []
for _ in range(count):
    w = input()
    words.append(w)

ans = Counter(words)

print(len(ans.keys()))

for w in ans:
    print(ans[w], end=" ")
    