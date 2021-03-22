import sys;

cnt = int(sys.stdin.readline());
arr = [];
for i in range(cnt):
    arr.append(int(sys.stdin.readline()));

arr.sort();
for i in arr:
    print(i);