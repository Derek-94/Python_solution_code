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
    needed_fountain = 0;
    garden = [0] * len(locations);
    fountain_ranges = [];
    for i in range(1, len(locations) + 1):
        max_location = max((i - locations[i - 1]), 1);
        min_location = min((i + locations[i - 1]), len(locations));
        fountain_ranges.append([min_location, max_location]);
    fountain_ranges.sort(key = lambda x: x[1]- x[0]);
           
    for fountain_range in fountain_ranges:
        print(fountain_range)
        start = fountain_range[1] - 1;        
        end = fountain_range[0] - 1;
        if garden[start] == 0 and garden[end] != 0:
            for i in range(start, end + 1):
                garden[i] += 1;
            needed_fountain += 1;
        elif garden[start] != 0 and garden[end] == 0:
            for i in range(start, end + 1):
                garden[i] = +1;
            needed_fountain += 1;
        elif garden[start] == 0 and garden[end] == 0:
            if sum(garden[start + 1:end]) > 0:
                max_garden = max(garden[start + 1:end]);
                for i in range(start, end + 1):
                    garden[i] = 1;
                needed_fountain -= max_garden;
                print("included.")
            else:
                for i in range(start, end + 1):
                    garden[i] += 1;
                needed_fountain += 1;
            
    print(garden)
    return needed_fountain
    

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
    dp = [-1] * len(locations);
 
    # Traverse the array
    for i in range(len(locations)):
        idxLeft = max(i - locations[i], 0)
        idxRight = min(i + (locations[i] + 1), len(locations))
        dp[idxLeft] = max(dp[idxLeft],idxRight)
        print(dp[idxLeft])
    print(dp)
    cntfount = 1;
 
    idxRight = dp[0]
 
    # Stores index of next fountain
    # that needed to be activated
    idxNext = 0
 
    # Traverse dp[] array
    for i in range(len(locations)):
        idxNext = max(idxNext, dp[i]);
 
        # If left most fountain
        # cover all its range
        if (i == idxRight):
            cntfount += 1
            idxRight = idxNext
 
    return cntfount
    

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
