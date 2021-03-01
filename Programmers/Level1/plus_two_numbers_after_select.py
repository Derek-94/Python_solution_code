def solution(numbers):
    answer = []
    
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j]);
    
    set_answer = set(answer);
    list_answer = list(set_answer);
    list_answer.sort();

    return list_answer;
