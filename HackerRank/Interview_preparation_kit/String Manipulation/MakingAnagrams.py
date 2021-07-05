#!/bin/python3

import math
import os
import random
import re
import sys
import collections
#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    a_cnt = collections.Counter(a);
    b_cnt = collections.Counter(b);
    return len(list((a_cnt - b_cnt).elements())) + len(list((b_cnt - a_cnt).elements()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
