#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):

    if len(ar) != 0:

        if len(ar) == 1:
            return ar[0]
        else:
            sum = 0
            for i in ar:
                sum += i
            return sum

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
