import math
def solution(brown, yellow):
    answer = [];
    
    arr = [];
    answer_arr = []
    
    for i in range(1, round(math.sqrt(yellow)) + 1):
        if yellow % i == 0:
            arr.append([i, yellow // i])
    
    for info in arr:
        if (info[0] * 2) + (info[1] * 2) + 4 == brown:
            answer_arr.append(info);
    
    if answer_arr[0][0] < answer_arr[0][1]:
        answer.append(answer_arr[0][1] + 2);
        answer.append(answer_arr[0][0] + 2);
    else:
        answer.append(answer_arr[0][0] + 2);
        answer.append(answer_arr[0][1] + 2);

    return answer