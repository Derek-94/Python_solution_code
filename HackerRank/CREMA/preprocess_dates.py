#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'preprocessDate' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY dates as parameter.
#

def convert_months(month):
    converted_month = '';
    if month == 'Jan':
        converted_month = '01';
    elif month == 'Feb':
        converted_month = '02';
    elif month == 'Mar':
        converted_month = '03';
    elif month == 'Apr':
        converted_month = '04';
    elif month == 'May':
        converted_month = '05';
    elif month == 'Jun':
        converted_month = '06';
    elif month == 'Jul':
        converted_month = '07';
    elif month == 'Aug':
        converted_month = '08';
    elif month == 'Sep':
        converted_month = '09';
    elif month == 'Oct':
        converted_month = '10';
    elif month == 'Nov':
        converted_month = '11';
    else:
        converted_month = '12';
    return converted_month;

def preprocessDate(dates):
    converted_result = [];
    # Write your code here
    for date in dates:
        day, month, year = date.split(" ");
        
        # Convert day first.
        converted_day = day[0:-2];
        if len(converted_day) == 1:
            converted_day = '0' + converted_day;
        
        # Then, convert month.
        converted_month = convert_months(month)
        
        # Years not needed to be converted.
        converted_result.append(year + '-' + converted_month + '-' + converted_day);
        
    return converted_result;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dates_count = int(input().strip())

    dates = []

    for _ in range(dates_count):
        dates_item = input()
        dates.append(dates_item)

    result = preprocessDate(dates)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
