import math;

def solution(n):
    answer = 0;
    
    candidate = math.sqrt(n);

    if int(candidate) - candidate == 0.0:
        answer = int((candidate + 1) ** 2);
    else:
        answer = -1
    
    return answer