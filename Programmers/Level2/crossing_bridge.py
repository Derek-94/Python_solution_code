def solution(stones, k):
    answer = 0;
    
    min_friend = 1;
    max_friend = 200000000;
    
    while min_friend <= max_friend:
        candidate = (min_friend + max_friend) // 2;
        
        cnt = 0;
        check = False;
        for i in stones:
            if i - candidate <= 0:
                cnt += 1;
            else:
                cnt = 0
            
            if cnt >= k:
                check = True;
                break;
        if check == True:
            max_friend = candidate - 1;
        else:
            min_friend = candidate + 1;
        
    return min_friend;