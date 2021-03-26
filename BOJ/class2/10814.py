import sys;

test_case = int(sys.stdin.readline());
arr = [];
for i in range(test_case):
    age, name = sys.stdin.readline().split();
    arr.append((int(age), name));

arr.sort(key = lambda x: (x[0]));

for i in arr:
    print(f'{i[0]} {i[1]}')