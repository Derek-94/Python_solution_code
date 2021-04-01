import heapq;
import sys;
cin = sys.stdin.readline;
arr = [];

cal_cnt = int(cin());
for _ in range(cal_cnt):
    command = int(cin());
    if command == 0:
        if len(arr) > 0:
            print(heapq.heappop(arr)[1]);
        else:
            print(0);
    else:
        heapq.heappush(arr, (-command, command));