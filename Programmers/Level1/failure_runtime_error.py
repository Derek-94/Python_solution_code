def solution(N, stages):
    answer = [];
    possiblities = [];
    total_user_num = len(stages);
    not_clear_user = [];
    
    for i in range(N + 1):
        not_clear_user.append(stages.count(i + 1));
    
    for i in range(N):
        possiblities += (i + 1, not_clear_user[i] / total_user_num);
        total_user_num -= not_clear_user[i];
        
    print(possiblities)
    
    return answer

solution(5, [2, 1, 2, 6, 2, 4, 3, 3]);