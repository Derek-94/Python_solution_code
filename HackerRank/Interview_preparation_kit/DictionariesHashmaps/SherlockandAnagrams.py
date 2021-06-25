#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    tmp = [];
    for i in range(1, len(s)):
        for j in range(0,len(s)-i+1):
            tmp.append("".join(sorted(s[j:j+i])));
    count = collections.Counter(tmp);
    print(count)
    return sum(sum(range(i)) for i in count.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
