def solution(priorities, location):
    answer = 0;
    
    arr = [(i, priorities) for i, priorities in enumerate(priorities)];
    
    while len(arr) > 1:
        item = arr.pop(0);
        max_item = max(arr, key=lambda x: x[1]);
        if item[1] < max_item[1]:
            # 다시 집어넣자. 
            arr.append(item);
        else:
            if location == item[0]:
                answer += 1;
                arr.append(item);
                break;
            else:
                answer += 1;
                
    if len(arr) == 1:
        answer += 1;
                
    return answer;