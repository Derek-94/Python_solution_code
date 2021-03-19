def solution(skill, skill_trees):
    answer = 0
    for sk in skill_trees:
        user_sk = [ alpha for alpha in sk if alpha in skill ]
        print(sk, user_sk)
        if skill.startswith(''.join(user_sk)):
            answer +=1
    return answer