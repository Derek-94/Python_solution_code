def solution(n):
    answer = 0;
    start_num = 0;
    
    while start_num != n:
        sum = 0;
        i = 0;
        start_num += 1;
        while True:
            sum += (start_num + i);
            if sum > n : 
                break;
            if sum == n:
                answer += 1;
                break
            i += 1;
    
    return answer