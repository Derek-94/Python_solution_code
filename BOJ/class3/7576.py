import sys;
import collections;
input = sys.stdin.readline;
tomato_arr = [];
answer = 0;
ready = collections.deque();
y, x = map(int, input().split());
for X in range(x):
    tmp = list(map(int, input().split()));
    for Y in range(y):
        if tmp[Y] == 1:
            ready.append([X, Y]);
    tomato_arr.append(tmp);

def bfs():
    global y, x, answer;
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];

    while ready:
        answer += 1;
        for _ in range(len(ready)):
            target_x, target_y = ready.popleft();

            for direction in dirs:
                nx = target_x + direction[0];
                ny = target_y + direction[1];

                if 0 <= nx < x and 0 <= ny < y and tomato_arr[nx][ny] == 0:
                    tomato_arr[nx][ny] = tomato_arr[target_x][target_y] + 1;
                    ready.append([nx, ny]);
    for row in tomato_arr:
        if 0 in row:
            return -1;
    return answer - 1;

print(bfs());