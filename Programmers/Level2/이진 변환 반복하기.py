def solution(s):
    transfer_cnt, zero_accumulate = 0, 0;
    
    while True:
        zero_count = s.count("0");
        modified_length = len(s) - zero_count;
        modified_bin = bin(modified_length)[2:];
        transfer_cnt += 1;
        zero_accumulate += zero_count;
        s = modified_bin;
        if modified_bin == "1":
            break;
    
    return [transfer_cnt, zero_accumulate]