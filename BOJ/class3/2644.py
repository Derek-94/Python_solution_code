import sys;
from collections import deque;
cin = sys.stdin.readline;
n = int(cin());
graph = [[0] * (n + 1) for i in range(n + 1)];
p1, p2 = map(int, cin().split());
relation_cnt = int(cin());
visited = [0] * n;

def bfs(start, goal):
    depth = 0;
    que = deque();
    que.append(start);
    while que:
        depth += 1;
        target = que.popleft();
        for i in range(n):
            if visited[i] == 0 and graph[i][target] != 0:
                que.append(i);
                visited[i] = 1;
                if i == goal:
                    return depth;

for _ in range(relation_cnt):
    x, y = map(int, cin().split());
    graph[x][y] = 1;
    graph[y][x] = 1;

print(min(bfs(p1, p2), bfs(p2, p1)));