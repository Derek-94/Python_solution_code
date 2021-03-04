def solution(strings, n):
    answer = [];
    
    for str in strings:
        answer.append(str[n] + str);
    
    answer.sort();
    for i in range(len(answer)):
        answer[i] = answer[i][1:];
        
    return answer