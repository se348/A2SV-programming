#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swap_count =0
    for j in range(len(a)):
        for i in range(len(a) -j +1):
            if i ==len(a) -1:
                break
            if(a[i]> a[i+1]):
                a[i], a[i+1] =a[i+1], a[i]
                swap_count +=1
    print(f"Array is sorted in {swap_count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a) -1]}")


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
