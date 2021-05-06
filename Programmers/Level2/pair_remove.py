def shrink(i, s):
    return s[:i] + s[i+2:];

def solution(s):
    answer = 0

    flag = False;
    
    while True:
        flag = False;
        for i in range(len(s)):
            if s[i] == s[i + 1]:
                s = shrink(i, s);
                flag = True;
                break;
        if flag == False:
            break;
    
    answer = 1 if len(s) == 0 else 0;

    return answer

def modified_solution(s):
    answer = 0

    stack = [];
    
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i]);
            # print(f'아무것도 없었다. 그냥 넣자. 결과는 {stack}');
        else:
            if stack[len(stack) - 1] == s[i]:
                stack.pop();
                # print(f'엇 같은게 있었다. 넣지 않았다. 있던것도 뺐다. {stack}');
            else:
                stack.append(s[i]);
                # print(f'걍 집어넣자. 결과는 {stack}')
    
    answer = 1 if len(stack) == 0 else 0;
    
    return answer
