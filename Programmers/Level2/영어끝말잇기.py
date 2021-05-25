import collections

def duplication_check(words, n):
    counter_list = collections.Counter(words);
    if counter_list.most_common()[0][1] != 1:
        dup_word = counter_list.most_common()[0][0];
        target_index = words[::-1].index(dup_word);
        target_index = len(words) - 1 - target_index;
        return ((target_index % n) + 1, ((target_index // n) + 1))
    else:
        return (0, 0);
    
def rules_check(total):
    prev_word = "";
    
    for i in range(len(total)):
        for j in range(len(total[i])):
            if prev_word == "":
                prev_word = total[i][j][len(total[i][j]) - 1];
            else:
                if prev_word != total[i][j][0]:
                    print("오류! 같지 않다.", prev_word, total[i][j][0]);
                    print(i, j)
                    return (j + 1, i + 1)
                else:
                    prev_word = total[i][j][len(total[i][j]) - 1];
    
    return (0, 0)

def solution(n, words):
    matrix = [];
    
    for i in range(0, len(words), n):
        cycle_arr = [];
        for j in range(i, i + n):
            if j <= len(words) - 1:
                cycle_arr.append(words[j]);
        matrix.append(cycle_arr);
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len(matrix[i][j]) == 1:
                return (j + 1, i + 1)
    
    dup_flag = duplication_check(words, n);
    if dup_flag == (0, 0):
        rule_flag = rules_check(matrix);        
        if rule_flag == (0, 0):
            return [0, 0];
        else:
            return rule_flag
    else:
        return dup_flag;
