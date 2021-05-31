def solution(n, s):
    answer = [];
    
    if n > s: return [-1];
    
    std = s // n;
    answer = [std] * n;
    
    remain = s % n;
    
    for i in range(remain):
        answer[len(answer) - 1 - i] += 1;
    
    return answer