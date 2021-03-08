def solution(s, n):
    answer = '';
    pushed_string = "";
    for i in range(len(s)):
        if s[i] == " ":
            answer += " ";
            continue;
        else:
            if ord(s[i]) >= 65 and ord(s[i]) <= 90:
                pushed_string = chr(ord(s[i]) + n);
                if ord(pushed_string) > 90:
                    pushed_string = chr(ord(pushed_string) - 90 + 65 - 1);
                answer += pushed_string;
            else:
                pushed_string = chr(ord(s[i]) + n);
                if ord(pushed_string) > 122:
                    pushed_string = chr(ord(pushed_string) - 122 + 97 - 1);
                answer += pushed_string;
    return answer