#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bitwiseEquations' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER_ARRAY b
def calculate(target_sum, target_xor):
    x = (target_sum - target_xor) // 2; # 
    y = target_sum - x;
    if bin(target_xor) == bin(x ^ y):
        return x, y;
    else:
        return 0, 0;

def bitwiseEquations(a, b):
    # Write your code here
    results = [];
    for i in range(len(a)):
        x, y = calculate(a[i], b[i]);
        results.append(2 * x + 3 * y);
    return results
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = int(input().strip())
        b.append(b_item)

    result = bitwiseEquations(a, b)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
