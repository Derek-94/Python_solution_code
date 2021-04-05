import sys;
from collections import deque;
cin = sys.stdin.readline;

def dfs(start):
    print(start, end = " ");
    for i in range(1, node + 1):
        if visit[i] == 0 and graph[start][i] == 1:
            visit[i] = 1;
            dfs(i);

def bfs(start):
    que = deque();
    que.append(start);
    while que:
        target = que.popleft();
        print(target, end=" ");
        for i in range(1, node + 1):
            if visit[i] == 0 and graph[target][i] == 1:
                que.append(i);
                visit[i] = 1;

node, link, start = map(int, cin().split());
graph = [[0] * (node + 1) for i in range(node + 1)];
for i in range(link):
    x, y = map(int, cin().split());
    graph[x][y] = 1;
    graph[y][x] = 1;
visit = [0 for i in range(node + 1)];

visit[start] = 1
dfs(start);
visit.clear();
visit = [0 for i in range(node + 1)];
visit[start] = 1
print();
bfs(start);