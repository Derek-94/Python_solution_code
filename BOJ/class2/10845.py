import sys;
command_cnt = int(sys.stdin.readline());
queue = [];

for i in range(command_cnt):
    command = str(sys.stdin.readline());
    if command.startswith("push"):
        command, target = command.split();
        queue.append(target);
    elif command.startswith("pop"):
        if len(queue) > 0:
            print(queue.pop(0));
        else:
            print(-1);
    elif command.startswith("back"):
        if len(queue) > 0:
            print(stack[len(queue) - 1]);
        else:
            print(-1);
    elif command.startswith("front"):
        if len(queue) > 0:
            print(queue[0]);
        else:
            print(-1)
    elif command.startswith("empty"):
        if len(queue) == 0:
            print(1);
        else:
            print(0);
    elif command.startswith("size"):
        print(len(queue));
