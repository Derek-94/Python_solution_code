def solution(n):
    answer = list(map(int, str(n)));
    answer.sort(reverse = True);
    final_answer = "".join(map(str, answer));
    
    return int(final_answer)