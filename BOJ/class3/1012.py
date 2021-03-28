import sys;
import collections
test_case = int(sys.stdin.readline());
que =  collections.deque();

dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

Y = 0;
X = 0;
answer = 0;

def bfs():
    global arr, que, dy, dx, Y, X;

    while que:
        y, x = que.popleft();
        for direction in dirs:
            ny, nx = y + direction[0], x + direction[1];
            if ny >= 0 and ny < Y and nx >= 0 and nx < X:
                if arr[ny][nx] == 1:
                    arr[ny][nx] = 0;
                    que.append([ny, nx]);

for _ in range(test_case):
    X, Y, plant_cnt = map(int, sys.stdin.readline().split());
    arr = [[0] * X for _ in range(Y)];
    
    for _ in range(plant_cnt):
        (plant_x, plant_y) = map(int, sys.stdin.readline().split());
        arr[plant_y][plant_x] = 1;
    
    for y in range(Y):
        for x in range(X):
            if arr[y][x] == 1:
                que.append([y, x]);
                bfs();
                answer += 1;
    print(answer);
    answer = 0;