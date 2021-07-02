#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fountainActivation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY locations as parameter.
#

def fountainActivation(locations):
    # Answer.
    fountain_cnt = 0;
    # Initialize dp array.
    dp = [-1] * len(locations);
 
    # Set all dp value to its maximum index.
    for i in range(len(locations)):
        min_index = max(i - locations[i], 0)
        max_index = min(i + (locations[i] + 1), len(locations))
        dp[min_index] = max(dp[min_index],max_index)
    
    # Indicies that will be turned on.
    switch_on_index = 0;
    # Save first end index.
    each_end_index = dp[0];
    
    for i in range(len(dp)):
        # Next swich on index is dp[i].
        if switch_on_index < dp[i]:
            switch_on_index = dp[i];
            
        # i became end index. -> increase fountain cnt.
        if i == each_end_index:
            fountain_cnt += 1;
            each_end_index = switch_on_index;
        
    return fountain_cnt + 1; # Add initial one.
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    locations_count = int(input().strip())

    locations = []

    for _ in range(locations_count):
        locations_item = int(input().strip())
        locations.append(locations_item)

    result = fountainActivation(locations)

    fptr.write(str(result) + '\n')

    fptr.close()
