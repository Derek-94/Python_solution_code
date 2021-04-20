def solution(n, times):
    answer = 0;
    start, end = 1, n*max(times);
    
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