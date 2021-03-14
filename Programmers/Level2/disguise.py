def solution(clothes):
    answer = 0;
    tup = {};
    for cloth in clothes:
        if cloth[1] in tup: tup[cloth[1]] += 1;
        else: tup[cloth[1]] = 1;
    
    acc = 1;
    for i in tup.values():
        acc *= (i + 1);
    answer = acc - 1
    return answer