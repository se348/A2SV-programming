#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    tempo = arr[n-1]
    idx = n-2
    
    while idx >= 0 and arr[idx] > tempo:
        arr[idx + 1] = arr[ idx ]
        idx -= 1
        print(*arr)
        
    if arr[idx] < tempo:
        arr[idx + 1] = tempo
    if idx <0:
        arr[0] = tempo
    print(*arr)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
