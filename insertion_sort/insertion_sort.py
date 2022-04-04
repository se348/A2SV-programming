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
    # Write your code here
    j= n-1
    k= n-2
    element =arr[j]
    while k >=0:
        if arr[k] >= element:
            arr[j] =arr[k]
            k-=1
            j-=1
        else:
            arr[j] =element
            for i in arr:
                print(i, end=" ")
            print('')
            break
        for i in arr:
            print(i, end=" ")
        print('')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
