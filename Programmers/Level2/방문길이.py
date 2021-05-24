def solution(dirs):
    answer = 0;
    arr = [[0] * 11 for i in range(11)];
    visited = [];
    cur_y, cur_x = 5, 5;
    
    for dir in dirs:
        if dir == 'U':
            ny = cur_y - 1;
            nx = cur_x;
            if 0 <= ny <= 10 and 0 <= nx <= 10:
                if (cur_y, cur_x, dir) not in visited:
                    visited.append((cur_y, cur_x, dir));
                    visited.append((ny, nx, 'D'));
                    answer += 1;
                cur_y, cur_x = ny, nx;
        elif dir == 'D':
            ny = cur_y + 1;
            nx = cur_x;
            if 0 <= ny <= 10 and 0 <= nx <= 10:
                if (cur_y, cur_x, dir) not in visited:
                    visited.append((cur_y, cur_x, dir));
                    visited.append((ny, nx, 'U'));
                    answer += 1;
                cur_y, cur_x = ny, nx;
        elif dir == 'L':
            ny = cur_y;
            nx = cur_x - 1;
            if 0 <= ny <= 10 and 0 <= nx <= 10:
                if (cur_y, cur_x, dir) not in visited:
                    visited.append((cur_y, cur_x, dir));
                    visited.append((ny, nx, 'R'));
                    answer += 1;
                cur_y, cur_x = ny, nx;
        else:
            ny = cur_y;
            nx = cur_x + 1;
            if 0 <= ny <= 10 and 0 <= nx <= 10:
                if (cur_y, cur_x, dir) not in visited:
                    visited.append((cur_y, cur_x, dir));
                    visited.append((ny, nx, 'L'));
                    answer += 1;
                cur_y, cur_x = ny, nx;

    return answer