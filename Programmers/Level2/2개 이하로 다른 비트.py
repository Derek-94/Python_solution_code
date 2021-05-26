def diff(std, big):
    cnt = 0;
    while len(std) != len(big):
        std = "0" + std;
    for i in range(len(std)):
        if std[i] == big[i]:
            continue;
        else:
            cnt += 1;
    return cnt;

def cal(n):
    bin_n = bin(n)[2:];
    i = 1;
    while True:
        bigger_n = n + i;
        tmp_bigger = bin(bigger_n)[2:];
        if diff(bin_n, tmp_bigger) <= 2:
            return bigger_n;
        else:
            i += 1;

def solution(numbers):
    answer = [];
    
    for num in numbers:
        result = cal(num);
        answer.append(result);
    
    return answer