def solution(s):
    answer = True;
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if ord(s[i]) <= 57 and ord(s[i]) >= 48:
                answer = True;
            else: 
                answer = False;
                break;
    else:
        answer = False;
    return answer