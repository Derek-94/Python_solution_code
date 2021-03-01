# #10952
while True:
    num1, num2 = list(map(int, input().split()));
    if((num1 == 0) and (num2 == 0)):
        break;
    else:
        print(num1 + num2);

# #1110
inputNum = input();
initial = ("0" + inputNum) if (len(inputNum) == 1) else inputNum;
cnt = 0;
cmp = 0;
while True:
    if(len(inputNum) == 1):
        inputNum = "0" + inputNum;
    sum = int(inputNum[0]) + int(inputNum[1]);
    if(len(str(sum)) > 1):
        sum = str(sum);
        sum = sum[1];
    cmp = inputNum[1] + str(sum);
    if(cmp == initial):
        break;
    else:
        cnt += 1;
        inputNum = cmp;
print(cnt + 1);

# #10951
while True:
    try:
        num1, num2 = map(int, input().split());
        print(num1 + num2);
    except:
        break;