import collections;
import sys;

def same_hertz(w):
    set_w = set(w);
    return len(set_w) == 1;

def v_hertz(wave):
    setWave = set(wave);
    if len(setWave) == 1:
        return 0;
    
    return sum([x ** 2 for x in wave]);
    
def roll(w):
    deq = collections.deque(w);
    front = deq.popleft();
    deq.append(front);
    return list(deq);

def concat_more(long_w, short_w):
    i = 0;
    longer_w = [];
    while(1):
        longer_w.append(short_w[i]);
        i += 1;
        if i == len(short_w):
            i = 0;
        if len(longer_w) == len(long_w):
            break;
    return longer_w;

def concat_wave_and_add(w1, w2):
    if len(w2) < len(w1):
        if(len(w1) % len(w2)) :
            long_w2 = concat_more(w1, w2);
            return [x + y for x, y in zip(w1, long_w2)];
        else:
            long_w2 = [];
            while len(long_w2) != len(w1):
                long_w2 = long_w2 + w2
            return [x + y for x, y in zip(w1, long_w2)];
    
    elif len(w1) < len(w2):
        if(len(w2) % len(w1)):
            long_w1 = concat_more(w2, w1);
            return [x + y for x, y in zip(long_w1, w2)];
        else:
            long_w1 = [];
            while len(long_w1) != len(w2):
                long_w1 = long_w1 + w1;
            return [x + y for x, y in zip(long_w1, w2)];
    else:
        return [x + y for x, y in zip(w1, w2)];

def pattern_check(w, pattern):
    if not len(w) % len(pattern) == 0:
        return False
    for i in range(0, len(w)):
        if not w[i] == pattern[i % len(pattern)]:
            return False
    return True;
    
def check_duplicate(w):
    for i in range(len(w) // 2):
        if pattern_check(w, w[0:i + 1]):
            return w[0:i + 1];
    return w;
    
def solution(wave1, wave2):
    answer = sys.maxsize;
        
    for _ in range(len(wave1)):
        wave1 = roll(wave1)
        for _ in range(len(wave2)):
            wave2 = roll(wave2);
            result = concat_wave_and_add(wave1, wave2);
            check_result = check_duplicate(result)
            answer = min(answer, v_hertz(check_result))
            
    return answer