def solution(n):
    answer = 0;
    cmp = bin(n).count("1")
    while True:
        n += 1;
        if cmp == bin(n).count("1"):
            break;
    
    return n