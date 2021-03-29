import sys;
import collections;
su, sis = map(int, sys.stdin.readline().split());
que = collections.deque();

def bfs():
    global su, sis, time, MAX;
    que = collections.deque();
    que.append(su);

    while que:
        target = que.popleft();
        if target == sis:
            print(time[target]);
            return;
        for i in [target - 1, target + 1, target * 2]:
            if 0 <= i < MAX and time[i] == 0:
                time[i] = time[target] + 1;
                que.append(i);

MAX = 100001
time = [0] * MAX;
bfs();