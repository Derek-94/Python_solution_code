def solution(a, b):
    answer = '';
    days = 0;
    
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    what_day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"];
    
    for i in range(a - 1):
        days += months[i];
    if a == 1:
        days -= 1;
    days += b;
    
    mod = days % 7;
    if a == 1:
        answer = what_day[mod];
    else:
        answer = what_day[mod - 1]
    
    return answer