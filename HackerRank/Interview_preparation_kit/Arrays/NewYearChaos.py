#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    moves = 0;
    q = [tmp - 1 for tmp in q];
    for index, val in enumerate(q):
        if val - index > 2:
            print('Too chaotic');
            return;
        for j in range(max(val-1,0),index):
            if q[j] > val:
                moves += 1
    print(moves)
        

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
