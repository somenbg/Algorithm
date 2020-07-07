#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    day_type = s[-2:]
    hour = s[:2]
    rest = s[2:-2]

    if day_type.upper() == 'PM':
        if int(hour) != 12:
            hour = str(int(hour) + 12)
        time = hour + rest
        return time
    
    if day_type.upper() == 'AM':

        if int(hour) == 12:
            hour = '00'
        time = hour + rest
        return time
    #

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    # f.write(result + '\n')

    # f.close()
