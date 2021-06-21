#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    cur_level = 0;
    valley_start = False;
    valley_cnt = 0;
    for step in range(steps):
        if path[step] == 'U':
            cur_level += 1;
            if valley_start == True and cur_level >= 0:
                valley_cnt += 1;
                valley_start = False;
        else:
            cur_level -= 1;
            if cur_level < 0:
                valley_start = True;
    return valley_cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
