def solution(arr1, arr2):
    answer = [];
    
    for y in range(len(arr1)):
        tmp = [];
        for x in range(len(arr1[0])):
            tmp.append(arr1[y][x] + arr2[y][x]);
        answer.append(tmp);
    
    return answer