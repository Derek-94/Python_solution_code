def solution(s):
    answer = '';
    arr = s.split(" ");
    for i in arr:
        if i == '':
            answer += " ";
        else:
            answer = answer + (i[0].upper() + i[1:].lower() + " ");
    answer = answer[:-1]
    
    
    return answer;