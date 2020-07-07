#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

    sum_all = 0

    for i in arr:
        sum_all += i

    max_sum = sum_all - min(arr)
    min_sum = sum_all - max(arr)

    # min_num = 0
    # max_num = 0

    # for num, i in enumerate(arr):

    #     if num == 0:
    #         min_num = i

    #     if i > max_num:
    #         max_num = i
    #     if i < min_num:
    #         min_num = i

    # max_sum = 0
    # min_sum = 0
    
    # for i in arr:

    #     if i != max_num:
    #         min_sum += i
    #     if i != min_num:
    #         max_sum += i


    print(min_sum, max_sum)
            

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
