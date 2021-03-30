import sys;

N = int(sys.stdin.readline());
arr = list(map(int, sys.stdin.readline().split()));
arr_sort = list(set(arr));
arr_sort.sort();
dic = {value: key for key, value in enumerate(arr_sort)}

for i in arr:
    print(dic[i], end=" ")