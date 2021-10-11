def solution(estimates, k):
    first_sum = sum(estimates[0:k]);
    prev_sum = first_sum;
    answer = first_sum;

    for i in range(0, len(estimates) - k):
        prev_sum = prev_sum - estimates[i] + estimates[i + k];
        answer = max(answer, prev_sum)       
        # answer = max(answer, sum(estimates[i:i+k]));
    
    return answer;

