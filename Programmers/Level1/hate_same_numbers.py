def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    answer.append(arr[0]);
    j = 0;
    
    for i in range(1,len(arr)):
        if answer[j] == arr[i]:
            continue;
        else:
            answer.append(arr[i]);
            j += 1;
    
    return answer;