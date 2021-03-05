def solution(s):
    answer = True
    
    lower_s = s.lower();
    
    p_count = lower_s.count("p");
    y_count = lower_s.count("y");
    

    if p_count == y_count and p_count > 0:
        return True
    else:
        return False;