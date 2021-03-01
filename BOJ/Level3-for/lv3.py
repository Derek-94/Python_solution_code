# #2739
num1 = int(input());
for i in range(1, 10):
    print(num1, "*", i, "=", num1*i);

# 10950
caseNum = int(input());
for i in range(1, caseNum + 1):
    num1, num2 = map(int, input().split());
    print(num1 + num2);

# 8393
inputNum = int(input());
sum = 0;
for i in range(1, inputNum + 1):
    sum += i;
print(sum);

# #15552
import sys
cases = int(input());

for i in range(cases):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)

# #2741
N = int(input());
for i in range(N, 0, -1):
    print(i);

# #11021
caseNum1 = int(input());
for i in range(1, caseNum1 + 1):
    num1, num2 = map(int, input().split());
    print("Case #",i, ": ", num1 + num2, sep="");

# #11022
caseNum2 = int(input());
for i in range(1, caseNum2 + 1):
    num1, num2 = map(int, input().split());
    print("Case #", i, ": ", num1, " + ", num2, " = ", num1+num2, sep="");

# #2438
inputStarNum = int(input());
for i in range(1, inputStarNum + 1):
    print("*" * i)

# #2439
inputStarNum1 = int(input());
for i in range(1, inputStarNum1 + 1):
    print(" "*(inputStarNum1-i) + "*"*i)

# #10871
total, std = map(int, input().split());
arr = list(map(int, input().split()));
for i in range(total):
    if(arr[i] < std):
        print(arr[i], end=" ");