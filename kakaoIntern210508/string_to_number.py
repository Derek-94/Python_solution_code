def alpha_to_num(s):
    if s == "zero":
        return "0";
    elif s == "one":
        return "1";
    elif s == "two":
        return "2";
    elif s == "three":
        return "3";
    elif s == "four":
        return "4";
    elif s == "five":
        return "5";
    elif s == "six":
        return "6";
    elif s == "seven":
        return "7";
    elif s == "eight":
        return "8";
    elif s == "nine":
        return "9";
    else:
        return -1;
        

def solution(s):
    answer = "";
    
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i];
        else:
            check_str = "";
            for j in range(i, len(s)):
                check_str += s[j];
                tmp = alpha_to_num(check_str);
                if(tmp != -1):
                    answer += tmp;
                    break;
    
    answer = int(answer)
    
    return answer