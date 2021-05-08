from collections import deque;
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]];

def BFS(y, x, place, visited):
    judge = True;
    deq = deque();
    deq.append((y, x, 0));
    visited[y][x] = 1;
    while len(deq) > 0 and judge == True:
        cur_y, cur_x, dist = deq.pop();
        for dir in dirs:
            ny = cur_y + dir[0];
            nx = cur_x + dir[1];
            ndist = dist + 1;
            if ny < 5 and ny >= 0 and nx < 5 and nx >= 0 and ndist <= 2 and place[ny][nx] != "X" and visited[ny][nx] == 0:
                if place[ny][nx] == "P":
                    judge = False;
                    break;
                else:
                    deq.append((ny, nx, ndist));
                    visited[ny][nx] = 1;
    return judge;

def solution(places):
    answer = [];
    p_cnt = [];
        
    for i, place in enumerate(places):
        stop = False;
        visited = [[0] * 5 for i in range(5)];
        print(place)
        for y in range(len(place)):
            for x in range(len(place[y])):
                if stop == True:
                    break;
                if place[y][x] == "P":
                    if BFS(y, x, place, visited) == False:
                        answer.append(0);
                        stop = True;
        if stop == False:
            answer.append(1);
    return answer;