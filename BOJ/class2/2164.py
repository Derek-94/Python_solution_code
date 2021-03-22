import sys;
from collections import deque;

card_cnt = int(sys.stdin.readline());
deq = deque();

for i in range(card_cnt):
    deq.append(i + 1);

while len(deq) > 1:
    deq.popleft();
    deq.append(deq.popleft());

print(deq[0])