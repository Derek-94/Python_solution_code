# #11654 아스키코드
print(ord(input()));

# #11720
num_len = int(input());
nums = list(input());
print(nums);
sum = 0;
for i in range(len(nums)):
    sum += int(nums[i]);
print(sum);

# #10809
alphabetArr = [-1 for i in range(26)];
input_str = input();
for i in range(len(input_str)):
    if(alphabetArr[ord(input_str[i]) - 97] == -1):
        alphabetArr[ord(input_str[i]) - 97] = i;
for i in range(len(alphabetArr)):
    print(alphabetArr[i], end=" ")

# #2675
case_num = int(input());
result = "";
for i in range(case_num):
    rep_num, target_str= input().split();
    for i in range(len(target_str)):
        result += (target_str[i] * int(rep_num));
    print(result);
    result = "";

# #1157
input_str = input();
input_str = input_str.lower();
alphabet_arr = [0 for i in range(26)];
for i in range(len(input_str)):
    alphabet_arr[ord(input_str[i]) - 97] += 1;
if(alphabet_arr.count(max(alphabet_arr)) == 1):
    print(chr(alphabet_arr.index(max(alphabet_arr)) + 65))
else:
    print("?")

# #1152
word_array = list(input().split());
print(len(word_array));

# #2908
num1, num2 = input().split();
num1_reverse = int(num1[::-1]);
num2_reverse = int(num2[::-1]);
print(num1_reverse) if num1_reverse > num2_reverse else print(num2_reverse);

# #5622
result = 0;
input_dial_array = list(input().lower());
dial_std = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"];
for i in range(len(input_dial_array)):
    for j in range(len(dial_std)):
        if input_dial_array[i] in dial_std[j]:
            result += (j+3);
print(result);

# #2941
croatia_word = input();
result = 0;
croatia_std = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="];
for i in croatia_std:
      croatia_word = croatia_word.replace(i, "@");
print(len(croatia_word));

# #1316
def check_group_word(word):
    for i in range(len(word)):
        if i == len(word) - 1:
            return 1;
        elif word[i] != word[i + 1] and word[i] in word[i + 1:]:
            return 0;
        else:
            continue;

case_num = int(input());
answer = 0;
for i in range(case_num):
    answer += check_group_word(input());
print(answer);