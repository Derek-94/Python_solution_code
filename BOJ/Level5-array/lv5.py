# #10818
cnt = int(input());
arr = list(map(int,input().split()));
arr.sort();
print(arr[0], arr[len(arr) - 1]);

# #2562
arr = [];
for i in range(9):
    arr.append(int(input()));
print(max(arr));
print(arr.index(max(arr)) + 1);

# #2577
arr = [0 for i in range(10)];
n1 = int(input());
n2 = int(input());
n3 = int(input());
result = n1 * n2 * n3;
result = str(result);
for i in range(len(result)):
    tmp = int(result[i]);
    arr[tmp] += 1;
for i in range(len(arr)):
    print(arr[i]);

# #3052
arr = [0 for i in range(42)];
ans = 0;
for i in range(10):
    inputNum = int(input());
    arr[(inputNum % 42)] += 1;
for i in range(len(arr)):
    if(not arr[i] == 0):
        ans += 1;
print(ans);

# #1546
cnt = int(input());
score = list(map(int, input().split()));
score.sort();
maxScore = max(score);
for i in range(cnt):
    score[i] = score[i] / maxScore * 100;
print(sum(score) / cnt);

# #8958
testCnt = int(input());
score = 0;
totalScore = 0;
flag = 0;
for i in range(testCnt):
    case = input();
    for i in range(len(case)):
        if(case[i] == "O" and flag == 0):
            score = 1;
            flag = 1;
            totalScore += score;
        elif(case[i] == "O" and flag == 1):
            score += 1;
            totalScore += score;
        elif(case[i] == "X"):
            score = 0;
            flag = 0;
    print(totalScore);
    score = 0;
    totalScore = 0;

# #4344
testCase = int(input());
scores = [];
avg = 0;
cnt = 0;
for i in range(testCase):
    scores = list(map(int, input().split()));
    studentNum = scores.pop(0);
    avg = sum(scores) / studentNum;
    for i in range(len(scores)):
        if(scores[i] > avg):
            cnt += 1;
    print("%.3f"%(round((cnt / studentNum) * 100, 3)) + "%")
    cnt = 0;
    scores = [];