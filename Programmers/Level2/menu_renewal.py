from itertools import combinations;
import collections;

def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for order in orders:
            for li in combinations(order, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        sorted_candidates = collections.Counter(candidates).most_common()
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)

def solution(orders, course):
    answer = [];
    
    for i in course:
        tmp = collections.Counter();
        for order in orders:
            print(collections.Counter(itertools.combinations(order, i))
        if len(tmp) == 0:
            continue;
        print(tmp)
        max_cnt = tmp.most_common(1)[0][1];
        if max_cnt > 2:
            continue;


        for k, v in tmp.items():
            if v == max_cnt:
                answer.append("".join(k));
    answer.sort()
            
            
            
            
            
    return answer