# #15596
def solve(list):
    sum = 0;
    for i in range(len(list)):
        sum += list[i];
    return sum;

# #4673
def cal_self_num(inputNum):
    stringfyInput = str(inputNum);
    sum = 0;
    for i in range(len(stringfyInput)):
        sum += int(stringfyInput[i]);
    sum += inputNum;
    return sum;

# arr = [0 for i in range(10000000)];

# for i in range(1, 10001):
#     arr[cal_self_num(i)] = 1;

# for i in range(1, 10001):
#     if(arr[i] == 0):
#         print(i);

# #1065
def judge_hanNum(num):
    num_stringfy = str(num);
    if(len(num_stringfy) == 1 or len(num_stringfy) == 2):
        return True;
    elif(len(num_stringfy) == 3):
        if((int(num_stringfy[0]) - int(num_stringfy[1])) == (int(num_stringfy[1]) - int(num_stringfy[2]))):
            return True;
        else:
            return False;

# test = int(input());
# cnt = 0;
# for i in range(1, test + 1):
#     if(judge_hanNum(i)):
#         cnt += 1;
# print(cnt)