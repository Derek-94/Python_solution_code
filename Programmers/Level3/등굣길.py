def solution(m, n, puddles):
    answer = 0;
    road = [[-1] * m for i in range(n)];
    for i in puddles:
        i[0] -= 1;
        i[1] -= 1;
        road[i[1]][i[0]] = 0;
    road[0][0] = 1;
    for y in range(0, n):
        for x in range(0, m):
            if x == 0 and y == 0: continue;
            if y == 0 and x != 0:
                # 윗줄
                if [y, x] not in puddles:
                    road[y][x] = road[y][x - 1];
                else:
                    road[y][x] = 0;
            elif x == 0 and y != 0:
                # 왼쪽줄
                if [y, x] not in puddles:
                    road[y][x] = road[y - 1][x]
                else:
                    road[y][x] = 0;
            else:
                if road[y][x] != 0:
                    road[y][x] = road[y - 1][x] + road[y][x - 1]
    print(road)
    
    return road[n - 1][m - 1] % 1000000007