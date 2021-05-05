def place(cnt):
    if cnt == 6:
        return 1;
    elif cnt == 5:
        return 2;
    elif cnt == 4:
        return 3;
    elif cnt == 3:
        return 4;
    elif cnt == 2:
        return 5;
    else:
        return 6;

def solution(lottos, win_nums):
    answer = [0, 0];
    cnt = 0;
    
    for i in range(len(lottos)):
        # print(f'{lottos[i]}이 {win_nums}에 있나요? {lottos[i] in win_nums}')
        if lottos[i] in win_nums:
            # print("@@여기다", lottos, lottos[i])
            #lottos.remove(lottos[i]);
            win_nums.remove(lottos[i]);
            # print(f'조정후 lotto는 {lottos} 당첨번호는 {win_nums}')
            cnt += 1;
    # print(cnt)
    answer[1] = place(cnt);
    
    for i in lottos:
        if i == 0:
            cnt += 1;
    answer[0] = place(cnt);
    
    return answer