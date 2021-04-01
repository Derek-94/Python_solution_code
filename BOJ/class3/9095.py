import sys;
cin = sys.stdin.readline;
case_num = int(cin());
ott = [1, 2, 4]
for i in range(3, 10):
    ott.append(ott[i - 3] + ott[i - 2] + ott[i - 1])
for i in range(case_num):
    n = int(cin())
    print(ott[n - 1])