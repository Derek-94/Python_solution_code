import sys;
command_cnt = int(sys.stdin.readline());
deq = [];

for i in range(command_cnt):
    command = str(sys.stdin.readline());
    if command.startswith("push_back"):
        command, target = command.split();
        deq.append(target);
    elif command.startswith("push_front"):
        command, target = command.split();
        deq.insert(0, target);
    elif command.startswith("pop_front"):
        if len(deq) > 0:
            print(deq.pop(0));
        else:
            print(-1);
    elif command.startswith("pop_back"):
        if len(deq) > 0:
            print(deq.pop());
        else:
            print(-1);
    elif command.startswith("back"):
        if len(deq) > 0:
            print(deq[len(deq) - 1]);
        else:
            print(-1);
    elif command.startswith("front"):
        if len(deq) > 0:
            print(deq[0]);
        else:
            print(-1)
    elif command.startswith("empty"):
        if len(deq) == 0:
            print(1);
        else:
            print(0);
    elif command.startswith("size"):
        print(len(deq));
