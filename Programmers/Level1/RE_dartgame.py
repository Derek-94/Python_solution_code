import re;

def solution(dartResult):
    answer = 0;
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)');
    # re.compile("정규식") --> 패턴객체를 반환함.
    dart = p.findall(dartResult);
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
        print(dart)

    answer = sum(dart)
    return answer
    
    
    return answer