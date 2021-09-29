def solution(road, n):
    candidate = [];
    left, right = 0, 0;
    first_0 = 999;
    repair_cnt = n;

    while right < len(road):        
        if road[right] == '1':
            right += 1;
            if right == len(road):
                candidate.append(len(road[left:right]));
                left, right = first_0 + 1, first_0 + 1;
                repair_cnt = n;
                first_0 = 999;
        elif road[right] == '0' and repair_cnt > 0:
            first_0 = min(first_0, right);
            right += 1;
            repair_cnt -= 1;
            if right == len(road):
                candidate.append(len(road[left:right]));
                left, right = first_0 + 1, first_0 + 1;
                repair_cnt = n;
                first_0 = 999;
        elif road[right] == '0' and repair_cnt == 0:
            candidate.append(len(road[left:right]));
            left, right = first_0 + 1, first_0 + 1;
            repair_cnt = n;
            first_0 = 999;
 

solution('001100', 5)