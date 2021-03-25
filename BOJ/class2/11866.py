import sys;
people_num, k = map(int, sys.stdin.readline().split());
arr = [i + 1 for i in range(people_num)];
answer = [];
modify_k = 0;

while len(arr) > 0:
    modify_k = k;
    if modify_k > len(arr):
        while modify_k > len(arr): 
            modify_k -= len(arr)
    answer.append(arr.pop(modify_k - 1));
    arr = arr[modify_k - 1:] + arr[0:modify_k - 1];

print("<", end="");
ans = ", ".join(map(str, answer));
print(ans, end="");
print(">")