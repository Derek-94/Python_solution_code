import math;
def power(n):
    root = math.sqrt(n);
    head = round(root);
    if root - head != 0:
        return -1;
    else:
        return 1;

def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        if power(i) == -1:
            answer += i;
        else:
            answer -= i;
    
    return answer