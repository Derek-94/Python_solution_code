import sys;

n, k = map(int, sys.stdin.readline().split());

m = 1;
s = 1;

for i in range(k):
    m *= (n - i);
for i in range(1, k + 1):
    s *= i;
print(m//s)