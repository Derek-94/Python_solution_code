#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def sum_hourglass(arr, y, x):
    return_sum = 0;
    for i in range(3):
        return_sum += arr[y][x + i];
    return_sum += arr[y + 1][x + 1];
    for i in range(3):
        return_sum += arr[y + 2][x + i];
    return return_sum;
    

def hourglassSum(arr):
    # Write your code here
    sum_arr = [];
    for y in range(4):
        for x in range(4):
            sum_arr.append(sum_hourglass(arr, y, x));
    return max(sum_arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
