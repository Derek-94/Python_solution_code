import sys;
from collections import deque;

def judge(target):
    deq = deque();
    for i in target:
        if i == "(":
            deq.append("(");
        elif i == ")" and len(deq) == 0:
            return False;
        elif i == ")" and len(deq) > 0:
            deq.popleft();
    if len(deq) == 0: return True;
    else: return False;


test_case = int(sys.stdin.readline());

for i in range(test_case):
    target = sys.stdin.readline();
    if judge(target) == True:
        print("YES");
    else:
        print("NO");