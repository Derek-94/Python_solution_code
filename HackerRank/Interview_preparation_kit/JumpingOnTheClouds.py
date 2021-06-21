#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c, n):
    steps = 0;
    cur_location = 0;
    while cur_location < n - 1:
        if cur_location + 2 <= n - 1 and c[cur_location + 2] == 1:
            cur_location += 1;
            steps += 1;
        elif cur_location + 2 <= n - 1 and c[cur_location + 2] == 0:
            cur_location += 2;
            steps += 1;
        else:
            cur_location += 1;
            steps += 1;
            
    return steps
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, n)

    fptr.write(str(result) + '\n')

    fptr.close()
