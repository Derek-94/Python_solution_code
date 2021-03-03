def oper(array, i, j, k):
    slice_result = array[i - 1:j];
    slice_result.sort();
    return slice_result[k - 1];

def solution(array, commands):
    answer = [];
    
    result = 0;
    
    for i in range(len(commands)):
        result = oper(array, commands[i][0], commands[i][1], commands[i][2]);
        answer.append(result);
    
    return answer