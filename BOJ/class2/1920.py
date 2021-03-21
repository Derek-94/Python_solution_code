import sys

def binary_search(arr, x):
    start = 0;
    end = len(arr) - 1;

    while start <= end:
        mid = (start + end) // 2;
        if x == arr[mid]:
            return 1;
        elif x > arr[mid]:
            start = mid + 1;
        elif x < arr[mid]:
            end = mid - 1;
    return 0;

cmp_num_count = int(input());
cmp_num = list(map(int, sys.stdin.readline().split()));
cmp_num.sort();
input_num_count = int(input());
input_num = list(map(int, sys.stdin.readline().split()));

for i in range(input_num_count):
    print(binary_search(cmp_num, input_num[i]))