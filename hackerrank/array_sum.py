#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    if len(ar) != 0:
        if len(ar) == 1:
            return ar[0]
        else:
            sum = 0
            for i in ar:
                sum += int(i)
            return sum
    #

if __name__ == '__main__':

    ar_count = int(input('Enter length of the array: '))

    ar = list(map(int, input('Enter the array elements (int), space-seperated: ').rstrip().split()))

    while len(ar) != ar_count:
        print('Error. Length of the array does not match the actual number of elements provided.')
        
        ar = list(map(int, input('Please re-enter: ').rstrip().split()))

    result = simpleArraySum(ar)
    print(result)

