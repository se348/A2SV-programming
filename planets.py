from collections import Counter
def process(llist, c):
    counts = Counter(llist)
    res = 0
    for v in counts.values():
        res +=min(v,c)
    print(res)

test_cases = int(input())
for _ in range(test_cases):
    length, c= list(map(int, input().split()))
    llist = list(map(int, input().split()))
    process(llist, c)
