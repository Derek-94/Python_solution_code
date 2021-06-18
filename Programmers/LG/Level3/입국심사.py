def solution(n, times):
    answer = 0;
    start, end = 1, n*max(times);
    # start 는 가장 빠른 시간, end는 가장 오래걸리는 심사위원한테
    # n 명이 모두 입국심사를 받는 것.
    
    while start <= end:
        mid = (start + end) // 2;
        count = 0;
        
        for time in times:
            count += (mid // time);
            if count >= n:
                break;
        
        if count >= n:
            end = mid - 1;
            answer = mid;
        else:
            start = mid + 1;
    
    return answer

print(solution(6, [7, 10]))