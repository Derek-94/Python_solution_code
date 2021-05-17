def solution(n):
    answer = 0;
    
    arr = [0 for i in range(n)];
    arr[0] = 1;
    arr[1] = 1;
    
    for i in range(2, n):
        arr[i] = arr[i - 1] + arr[i - 2];
    answer = arr[n-1] % 1234567
        
    
    return answer