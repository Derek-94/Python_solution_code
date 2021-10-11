from collections import deque;

def solution(N, coffee_times):
    answer = [];
    process_deq = deque();
    
    if N == 1:
        return [i for i in range(1, len(coffee_times) + 1)];
    
    coffee_times_en = deque();
    for index, ele in enumerate(coffee_times):
        coffee_times_en.append((index + 1, ele));
    
    while len(answer) < len(coffee_times):
        while len(coffee_times_en) and len(process_deq) < N:
            process_deq.append(coffee_times_en.popleft());
        
        tmp_dep = deque();

        for index, time in process_deq:
            tmp_dep.append((index, time - 1));
        
        process_deq.clear();
        for index, time in tmp_dep:
            if time > 0:
                process_deq.append((index, time));
            else:
                answer.append(index);

    return answer

solution(3, [4, 2, 2, 5, 3]);