def solution(phone_number):
    answer = '';
    star_cnt = len(phone_number) - 4;
    answer = "*" * star_cnt + phone_number[star_cnt:];
    return answer