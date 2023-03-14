#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def helper(n):
    add = 0
    for i in range(len(n)):
        add += int(n[i])
    
    str_ver =str(add)
        
    if len(str_ver) == 1:
        return str_ver
    return helper(str_ver)
    
    
def superDigit(n, k):
    temp = []
    curr = helper(n) *k
    return helper(curr)
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
