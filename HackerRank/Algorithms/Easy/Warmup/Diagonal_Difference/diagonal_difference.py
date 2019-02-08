#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    diag_1 = 0
    diag_2 = 0
    size = len(arr)-1
    for i in range(size+1):
        diag_1 += arr[i][i]
        diag_2 += arr[i][size-i]
    return abs(diag_1-diag_2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
