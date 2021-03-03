def solution(answers):
    answer = [];
    p1 = [1, 2, 3, 4, 5];
    p2 = [2, 1, 2, 3, 2, 4, 2, 5];
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    personScore = [0, 0, 0];
    
    for i in range(len(answers)):
        if p1[i % 5] == answers[i]:
            personScore[0] += 1;
        if p2[i % 8] == answers[i]:
            personScore[1] += 1;
        if p3[i % 10] == answers[i]:
            personScore[2] += 1;
    
    maximum_score = max(personScore);
    
    for i in range(3):
        if personScore[i] == maximum_score:
            answer.append(i + 1);
    
    return answer;