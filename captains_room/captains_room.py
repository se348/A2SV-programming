# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
_ = input()
word = input()
res= word.split(" ")
vals= Counter(res)
for key, val in vals.items():
    if val==1:
        print(key)
