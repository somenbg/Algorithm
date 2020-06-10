#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):

    a_wins = 0
    b_wins = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            a_wins += 1
        if a[i] < b[i]:
            b_wins += 1
    
    return [a_wins,b_wins]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input('Enter Player 1 scores(space-separated): ').rstrip().split()))

    b = list(map(int, input('Enter Player 2 scores(space-separated): ').rstrip().split()))

    result = compareTriplets(a, b)
    print('The results are [Player 1, Player 2]: {}'.format(result))
    
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
