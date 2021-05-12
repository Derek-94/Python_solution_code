def solution_wrong(N, stages):
    answer = [];
    possibilities = [];
    total_user_num = len(stages);
    not_clear_user = [];
    min = -1;
    
    for i in range(N + 1):
        not_clear_user.append(stages.count(i + 1));
    
    for i in range(N):
        possibilities.append(not_clear_user[i] / total_user_num);
        total_user_num -= not_clear_user[i];
        
    print(possibilities)
    sorted_poss = sorted(possibilities, reverse = True)
    print(sorted_poss)
    
    for i in range(len(sorted_poss)):
        for j in range(len(possibilities)):
            if sorted_poss[i] == possibilities[j]:
                answer.append(j + 1);
                possibilities[j] = -1;
                break;
    
    return answer;

import collections;

def solution_right(N, stages):
    answer = [];
    failure = {};
    user_num = len(stages);
    
    counter_stage = collections.Counter(stages);
    print(counter_stage);
    
    for i in range(1, N + 1):
        if counter_stage[i] != 0:
            i_th_fail_num = counter_stage[i];
            failure[i] = i_th_fail_num / user_num;
            user_num -= i_th_fail_num;
        else:
            failure[i] = 0;
    print(failure);
    
    sort_failure = sorted(failure.items(), key = lambda x: (x[1]), reverse = True)
    
    for i in sort_failure:
        answer.append(i[0]);
    
    return answer