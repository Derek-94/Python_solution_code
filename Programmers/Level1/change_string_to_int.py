def solution(s):
    answer = 0
    
    if s[0] == "-":
        only_num = s[1:];
        answer = int(only_num);
        answer = -answer
    else:
        answer = int(s);

    return answer