import math;
import itertools;

def check_prime_number(num):
    if num <= 1: return 0;
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0;
    return 1;

def solution(numbers):
    answer = 0;
    check_waiting = [];
    check_new = [];
    set_check = set();
    
    for i in range(1, len(numbers) + 1):
        check_waiting.append(list(map(int,map("".join, itertools.permutations(numbers, i)))));
    
    for num in check_waiting:
        for i in num:
            check_new.append(i)
            
    set_check = set(check_new);
    
    for i in set_check:
        if check_prime_number(i) == 1:
            answer += 1;
    
    return answer