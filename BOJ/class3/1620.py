import sys;
pok_num, problem_num = map(int, sys.stdin.readline().split());
pok = [];
pok_dic = {};
for i in range(pok_num):
    pokemon = sys.stdin.readline().rstrip()
    pok.append((i, pokemon));
    pok_dic[pokemon] = i
for i in range(problem_num):
    tmp = sys.stdin.readline().rstrip();
    if tmp.isdigit():
        print(pok[int(tmp) - 1][1]);
    else:
        print(pok_dic[tmp] + 1)