from collections import deque;

def solution(t, r):
    answer = [];
    info = [];
    del_index = [];
    
    for i in range(len(t)):
        info.append((t[i], r[i], i));
    
    time = 0;
    tmp = deque();
    print("시작.")
    while len(info):
        #print("현재 상태는", info, "현재 시간은", time);
        for i in range(len(info)):
            if info[i][0] <= time:
                #print("조정한다. info 삭제하고, tmp는 늘린다.");
                tmp.append(info[i]);
                #print("결과 info는", info, "tmp는", tmp);
        for t in tmp:
            if t in info:
                del info[info.index(t)]
        #print(time, "이하인 애들 넣은 배열은", tmp, "info는 ->", info);
        tmp_list = list(tmp);
        tmp_list.sort(key = lambda x: (x[1], x[0], x[2]));
        tmp = deque(tmp_list)
        #print("정렬하고 나서 는", tmp)
        if len(tmp) > 0:
            answer.append(tmp.popleft()[2]);
        #print("answer는", answer)
        time += 1;
    
    return answer

solution([0, 0, 1], [0, 1, 1]);