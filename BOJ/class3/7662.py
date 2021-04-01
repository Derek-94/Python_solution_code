import sys;
from queue import PriorityQueue;

que = PriorityQueue();
input = sys.stdin.readline;
test_case = int(input());
for _ in range(test_case):
    input_num = int(input());
    for i in range(input_num):
        command = input();
        if command.startswith("I"):
            # push
        else:
            command_prev, command_after = command.split();
            if command_after == "1":
                # print max
            else:
                # print min