import math;

def judge(n):
    for i in range(2, round(math.sqrt(n))+1):
        if n % i == 0 :
            return False;  
        else:
            continue;
    return True;

def solution(n):
    answer = 0;
    
    for i in range(2, n + 1):
        if judge(i) == True:
            answer += 1;
            
    return answer