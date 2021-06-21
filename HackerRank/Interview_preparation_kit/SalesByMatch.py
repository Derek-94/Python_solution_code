#!/bin/python3

import math
import os
import random
import collections
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    pair_cnt = 0;
    # Write your code here
    li_counter = list(collections.Counter(ar).items());
    for i in li_counter:
        key = i[0];
        val = i[1];
        while val >= 2:
            pair_cnt += 1;
            val -= 2;
    return pair_cnt
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
