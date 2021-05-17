import re;
import math;
from collections import Counter;

def solution(str1, str2):
    answer = 0;
    and_cnt = 0;
    or_cnt = 0;
    reg = '[^a-zA-Z]'
    # a ~ z, A ~ Z 가 아닌애를 찾으면 18번째 줄에서 continue.
    
    str1_arr = [];
    str2_arr = [];
    
    for i in range(len(str1) - 1):
        tmp1 = str1[i] + str1[i + 1];
        if re.search(reg, tmp1):
            continue;
        else:
            str1_arr.append(tmp1.lower());
    for i in range(len(str2) - 1):
        tmp2 = str2[i] + str2[i + 1];
        if re.search(reg, tmp2):
            continue;
        else:
            str2_arr.append(tmp2.lower());
    
    c1 = Counter(str1_arr);
    c2 = Counter(str2_arr);
    
    for i in c1:
        if c2[i] >= 1:
            if c1[i] >= c2[i]:
                and_cnt += c2[i];
                c2[i] = 0;
                c1[i] -= c2[i]
            else:
                and_cnt += c1[i];
                c1[i] = 0;
                c2[i] -= c1[i]
    
    plus = c1 + c2;
    or_cnt = sum(plus.values());
    if (and_cnt == 0 and or_cnt == 0):
        return 65536 
    answer = math.floor(and_cnt / or_cnt * 65536);
    
    return answer