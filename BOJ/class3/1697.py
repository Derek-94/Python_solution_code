import sys;
from collections import deque;
LIMIT = 100001

def bfs(time, su, sis):
    que = deque();
    que.append(su);

    while que:
        target = que.popleft();
        if target == sis:
            print(time[target]);
            return;
        for next_step in [target - 1, target + 1, target * 2]:
            if time[next_step] == 0 and (0 <= next_step < LIMIT):
                time[next_step] = time[target] + 1;
                que.append(next_step);

su, sis = map(int, sys.stdin.readline().split());
time = [0] * LIMIT;
bfs(time, su, sis);