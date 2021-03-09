def solution(d, budget):
    answer = 0;
    sum = 0;
    
    d.sort();
    
    for i in range(len(d)):
        if d[i] + sum <= budget:
            sum += d[i];
            answer += 1;
    
    return answer