import sys;
import collections;
cin = sys.stdin.readline;
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)];
answer = 0;
while True:
    w, h = map(int, cin().split());
    if w == 0 and h == 0:
        break;
    map_arr = [];
    for y in range(h):
        map_arr.append(list(map(int, cin().split())));
    visited = [[0] * w for _ in range(h)];

    def bfs(y, x):
        global answer;
        que = collections.deque();
        que.append((y, x));
        while que:
            target_y, target_x = que.popleft();
            for dir in dirs:
                ny, nx = target_y + dir[0], target_x + dir[1];
                if 0 <= ny < h and 0 <= nx < w and visited[ny][nx] == 0:
                    if map_arr[ny][nx] == 1:
                        que.append((ny, nx));
                        visited[ny][nx] = 1;
        answer += 1;


    for y in range(h):
        for x in range(w):
            if map_arr[y][x] == 1 and visited[y][x] == 0:
                visited[y][x] = 1;
                bfs(y, x);
    print(answer);
    visited.clear();
    answer = 0;