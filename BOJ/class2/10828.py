import sys;
command_cnt = int(sys.stdin.readline());
stack = [];

for i in range(command_cnt):
    command = str(sys.stdin.readline());
    if command.startswith("push"):
        command, target = command.split();
        stack.append(target);
    elif command.startswith("pop"):
        if len(stack) > 0:
            print(stack.pop());
        else:
            print(-1);
    elif command.startswith("top"):
        if len(stack) > 0:
            print(stack[len(stack) - 1]);
        else:
            print(-1);
    elif command.startswith("empty"):
        if len(stack) == 0:
            print(1);
        else:
            print(0);
    elif command.startswith("size"):
        print(len(stack));
