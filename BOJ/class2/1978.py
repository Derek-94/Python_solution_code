import math
def prime_num(n):
    if n <= 1: return 0;
    elif n == 2 : return 1;
    for i in range(2, round(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0;
    return 1;

cnt = int(input());
arr = [];
answer = 0;

arr = list(map(int, input().split()));

for num in arr:
    if prime_num(num) == 1:
        answer += 1;

print(answer);