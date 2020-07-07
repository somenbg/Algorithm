#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):

    zero_count = 0
    positive_count = 0
    negative_count = 0
    total_count = len(arr)

    if len(arr) != 0:
        for i in arr:
            if i > 0:
                positive_count += 1
            elif i < 0:
                negative_count += 1
            else:
                zero_count += 1
    
    print(format(positive_count/total_count, '.5f'))
    print(format(negative_count/total_count, '.5f'))
    print(format(zero_count/total_count, '.5f'))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
