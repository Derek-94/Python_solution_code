def solution(s):
    std = "()";
    
    queue = [];
    
    for i in s:
        if i == "(":
            queue.append("(");
        else:
            try:
                queue.pop();
            except:
                return False;
    
    if len(queue) == 0:
        return True;
    else: return False;
    
#     while True:
#         if s.find("()") == -1:
#             break;
#         else:
#             s = s.replace("()", "");
    
#     if len(s) == 0:
#         return True;
#     else:
#         return False;
