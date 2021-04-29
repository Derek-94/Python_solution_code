from collections import Counter;
import re;
def solution(s):
    answer = [];
    
    s = re.sub('[{}]', "", s)
    arr = list(s.split(","))
    arr_counter = Counter(arr).most_common()
    
    for i in arr_counter:
        answer.append(int(i[0]))
    
    return answer