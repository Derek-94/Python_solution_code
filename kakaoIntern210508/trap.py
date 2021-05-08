from collections import deque;

def reverse(n, roads):
    reversed_roads = [];
    for i in roads:
        if i[0] == n or i[1] == n:
            reversed_roads.append((i[1], i[0], i[2]));
        else:
            reversed_roads.append(i);
    return reversed_roads;
            
            
def bfs(n, start, end, roads, traps):
    que = deque();
    cnt = 0;
    que.append((start, cnt));
    
    while len(que) > 0:
        cur, cur_dist = que.popleft();
        if(cur == end): return cur_dist;
        if cur in traps:
            roads = reverse(cur, roads);
        for road in roads:
            if road[0] == cur:
                que.append((road[1], cur_dist + road[2]));
                if road[1] == end: return cur_dist + road[2];

def solution(n, start, end, roads, traps):
    answer = 0;
    answer = bfs(n, start, end, roads, traps)
    
    return answer

solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]]	, [2, 3])