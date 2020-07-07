#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):

    for i in range(n):
        pad = '#' * (i+1)
        print(pad.rjust(n, ' '))


if __name__ == '__main__':
    n = int(input('Enter a number for the base/height: '))

    staircase(n)
