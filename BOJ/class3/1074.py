import sys;
n, r, c = map(int, sys.stdin.readline().split());

size = pow(2, n);

arr = [[0] * size for i in range(size)];
print(arr);