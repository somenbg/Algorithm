#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    num = 0
    count = 0
    for i in ar:
        
        # check if multiple same element exists i.e. number of candles that can be blown
        if num == i:
            count += 1

        # loop to find the largest element in the array and reseting count everytime there is a larger number
        if i > num:
            num = i
            count = 0

    return count + 1

    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
