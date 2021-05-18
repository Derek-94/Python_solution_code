def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for i in range(len(arr1))];
    
    
    for k in range(len(arr1)):
        for y in range(len(arr2[0])):
            for x in range(len(arr1[0])):
                answer[k][y] += (arr1[k][x] * arr2[x][y])
            
    print(answer)
        
    return answer