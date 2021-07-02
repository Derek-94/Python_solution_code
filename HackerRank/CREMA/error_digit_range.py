#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findRange' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER num as parameter.
#
def find_max(num):
    # Simple. just convert first num to 9, if it is not 9.
    convert_target_index = -1;
    for i in range(len(num)):
        if num[i] != '9':
            convert_target_index = i;
            break;
    converted_num = num.replace(num[convert_target_index], '9');
    return int(converted_num);
    
def find_min(num):
    # Seperate cases in 2.
    # 1. First num is NOT '1':
    #   - Convert first num in '1'.
    # 2. First num is '1':
    #   - Begin checking from index 2, if it is not 0, and not same with first one.
    if num[0] != '1':
        return int(num.replace(num[0], '1'));
    else:
        convert_target_index = -1;
        for i in range(1, len(num)):
            if num[i] != '0' and num[i] != num[0]:
                convert_target_index = i;
                break;
            
            elif i == len(num) - 1: # if all the numbers all same, we just change number to 1....1.
                return int(num.replace(num[0], '1'))
        converted_num = num.replace(num[convert_target_index], '0');
        return int(converted_num)
    
def findRange(num):
    # If num is smaller than 10, just return 9 - 1, 8.
    if num < 10:
        return 8;
        
    # Conversion Starts.
    stringfy_num = str(num);
    # find_XXX functions will handles getting each values.
    maximum = find_max(stringfy_num);
    minimum = find_min(stringfy_num);
    return maximum - minimum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num = int(input().strip())

    result = findRange(num)

    fptr.write(str(result) + '\n')

    fptr.close()
