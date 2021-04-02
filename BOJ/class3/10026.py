import sys;
import collections;
cin = sys.stdin.readline;
N = int(cin());
pic = [];
visited = [[0] * N for i in range(N)];
que = collections.deque();
color_cnt = 0;
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];

for y in range(N):
    pic.append(list(cin().rstrip()));

def bfs(pic, visited, que, color):
    global color_cnt;
    while que:
        cur_x, cur_y = que.popleft();
        for direction in dirs:
            nx, ny = cur_x + direction[0], cur_y + direction[1];
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if pic[nx][ny] == color:
                    visited[nx][ny] = 1;
                    que.append((nx, ny));
    color_cnt += 1;
    
for y in range(N):
    for x in range(N):
        if visited[y][x] == 0:
            que.append((y, x));
            bfs(pic, visited, que, pic[y][x]);
print(color_cnt, end=" ");

for y in range(N):
    for x in range(N):
        if pic[y][x] == "R" or pic[y][x] == "G":
            pic[y][x] = "C";

color_cnt = 0;
visited = [[0] * N for i in range(N)];
que.clear();
for y in range(N):
    for x in range(N):
        if visited[y][x] == 0:
            que.append((y, x));
            bfs(pic, visited, que, pic[y][x]);
print(color_cnt);