#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here

    # matrix_shape = len(arr)
    # matrix_col_num = len(arr[matrix_row_num - 1])
    l_to_r = 0
    r_to_l = 0

    for i in range(len(arr)):

        l_to_r += arr[i][i]
        r_to_l += arr[i][-(i+1)]

    return abs(l_to_r - r_to_l)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
    
    # fptr.write(str(result) + '\n')

    # fptr.close()
