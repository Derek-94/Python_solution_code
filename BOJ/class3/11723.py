import sys;
cin = sys.stdin.readline;

S = set();

cal_cnt = int(cin());

for _ in range(cal_cnt):
    command = cin().strip().split();
    if len(command) == 1:
        if command[0] == "all":
            S = {i + 1 for i in range(20)}
            print(S)
        else:
            S = set();
    else:
        com, target = command[0], int(command[1]);
        if com == "add":
            S.add(target);
        elif com == "remove":
            S.discard(target)
        elif com == "check":
            if target in S:
                print(1);
            else:
                print(0);
        elif com == "toggle":
            if target in S:
                S.remove(target);
            else:
                S.add(target);