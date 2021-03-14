import collections
def solution(people, limit):
    answer = 0;
    people.sort();
    measure = 0;
    deq = collections.deque(people);
    
    while len(deq) > 0:
        max_weight =  deq.pop();
        measure += max_weight;
        
        while len(deq) > 0 and measure + deq[0] <= limit:
            measure += deq.popleft();
            
        measure = 0;
        answer += 1;
    
    return answer