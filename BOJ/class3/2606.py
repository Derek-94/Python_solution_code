import sys;
import collections;
input = sys.stdin.readline;
computer_cnt = int(input());
computer_visited = [0 for i in range(computer_cnt + 1)];
pair_cnt = int(input());
answer = 0;

que = collections.deque();
connection_state = [];

computer_visited[1] = 1;
for _ in range(pair_cnt):
    com1, com2 = map(int, input().split());
    connection_state.append((com1, com2));
    if com1 == 1 and computer_visited[com2] == 0:
        que.append(com2);
        computer_visited[com2] = 1;
    elif com2 == 1 and computer_visited[com1] == 0:
        que.append(com1);
        computer_visited[com1] = 1;

answer += len(que);

while que:
    cur = que.popleft();
    for i in range(pair_cnt):
        if cur in connection_state[i]:
            if connection_state[i][0] == cur and computer_visited[connection_state[i][1]] == 0:
                que.append(connection_state[i][1]);
                computer_visited[connection_state[i][1]] = 1;
                answer += 1;
            elif connection_state[i][1] == cur and computer_visited[connection_state[i][0]] == 0:
                que.append(connection_state[i][0]);
                computer_visited[connection_state[i][0]] = 1;
                answer += 1;
print(answer);

