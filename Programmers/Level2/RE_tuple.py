from collections import Counter;
import re;
def solution(s):
    answer = [];
    
    s = re.sub('[{}]', "", s)
    # re.sub("정규표현식", 이렇게 바꿀거야, 목표 문자열)
    arr = list(s.split(","))
    arr_counter = Counter(arr).most_common()
    
    for i in arr_counter:
        answer.append(int(i[0]))
    
    return answer