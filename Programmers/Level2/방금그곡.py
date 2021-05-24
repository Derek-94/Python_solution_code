def modify_m(m):
    result = '';
    flag = False;
    for i in range(1, len(m)):
        if flag:
            flag = False;
            continue;
        if m[i] != '#':
            result += m[i - 1];
        else:
            result += m[i - 1].lower();
            flag = True;
    if m[len(m) - 1] == '#':
        return result;
    else:
        result += m[len(m) - 1];
        return result

def cal_duration(s, e):
    s_hour, s_min = s.split(":");
    e_hour, e_min = e.split(":");
    s_hour, s_min, e_hour, e_min = int(s_hour), int(s_min), int(e_hour), int(e_min);
    while s_hour != e_hour:
        e_hour -= 1;
        e_min += 60;
    return e_min - s_min;

def total_compose(t, melody):
    tmp = '';
    melody = modify_m(melody);
    for i in range(t):
        tmp += melody[i % len(melody)];
    return tmp;

def cmp(e):
    start, end, music_title, melody = e.split(",");
    dur = cal_duration(start, end);
    return -dur;
        
def solution(m, musicinfos):
    m = modify_m(m);
    print(m)
    answer = '';
    dic = {};
    
    musicinfos.sort(key = cmp);
    
    for i in musicinfos:
        tmp = '';
        start, end, music_title, melody = i.split(",");
        play_time = cal_duration(start, end);
        music_note = total_compose(play_time, melody);
        print(play_time, music_note)
        dic[music_title] = music_note;
    
    for i in dic:
        if m in dic[i]:
            answer += i;
            break;
    if len(answer) == 0:
        answer += '(None)'

    return answer