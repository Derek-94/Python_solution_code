import sys;
heard, seen = map(int, sys.stdin.readline().split());
heard_arr = [];
seen_arr = [];
answer_arr = [];
for _ in range(heard):
    heard_arr.append(sys.stdin.readline().rstrip());
for _ in range(seen):
    seen_arr.append(sys.stdin.readline().rstrip());
answer_arr = list(set(heard_arr) & set(seen_arr));
print(len(answer_arr));
answer_arr.sort();
for i in answer_arr:
    print(i);