def transfer(n, target):
    result = "";
    while target >= 1:
        target, remain = divmod(target, n);
        if remain == 10:
            remain = 'A';
        elif remain == 11:
            remain = 'B';
        elif remain == 12:
            remain = 'C';
        elif remain == 13:
            remain = 'D';
        elif remain == 14:
            remain = 'E';
        elif remain == 15:
            remain = 'F';
        else:
            pass;
        result += str(remain);
        
    return result[::-1];
    

def solution(n, t, m, p):
    answer = '';
    max_num = t * m;
    total_ans = "0";
    
    for i in range(max_num):
        total_ans += transfer(n, i);
    
    for i in range(p - 1, max_num, m):
        answer += total_ans[i];
        if len(answer) == t:
            return answer

