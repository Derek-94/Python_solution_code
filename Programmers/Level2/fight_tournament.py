def solution(n,a,b):
    answer = 0
    while a!=b:
        print(a, b)
        a= (a+1)//2
        b= (b+1)//2
        print(a, b)
        answer+=1
    return answer