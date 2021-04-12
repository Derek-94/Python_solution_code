import sys;
import collections;
cin = sys.stdin.readline;
test_case = int(cin());
answer = 0;

dirs = [(-2, 1), (-1, 2), (1, 2), (2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)];

def bfs(y, x):
    global answer;
    que = collections.deque();
    que.append((y, x));
    if y == goal_y and x == goal_x:
        return 0;
    while que:
        y, x = que.popleft();
        for dir in dirs:
            ny, nx = y + dir[0], x + dir[1];
            if 0 <= ny < length and 0 <= nx < length and visited[ny][nx] == 0:
                if ny == goal_y and nx == goal_x:
                    return visited[y][x] + 1;
                else:
                    que.append((ny, nx));
                    visited[ny][nx] = visited[y][x] + 1;


for _ in range(test_case):
    length = int(cin());
    visited = [[0] * length for _ in range(length)];
    y, x = map(int, cin().split());
    goal_y, goal_x = map(int, cin().split());
    print(bfs(y, x));