def solution(record):
    answer = [];
    
    result_list = [];
    revised = False;
    user_dic = {}
    
    for rec in record:
        if rec.startswith("Enter"):
            id = rec.split(" ")[1];
            user = rec.split(" ")[2];
            result_list.append([f'{id} Enter', f'{user}님이 들어왔습니다.']);
            for i in range(len(result_list)):
                if f'{id} Enter' == result_list[i][0]:
                    result_list[i][1] = f'{user}님이 들어왔습니다.'
                    user_dic[id] = user;
                    revised = True;
                if f'{id} Leave' == result_list[i][0]:
                    result_list[i][1] = f'{user}님이 나갔습니다.';
            if revised == False:
                user_dic[id] = user;
            revised = False;
        elif rec.startswith("Leave"):
            id = rec.split(" ")[1];
            user_name = user_dic[id];
            result_list.append([f'{id} Leave', f'{user_name}님이 나갔습니다.']);
        else:
            id = rec.split(" ")[1];
            new_username = rec.split(" ")[2];
            user_dic[id] = new_username;
            for i in range(len(result_list)):
                if f'{id} Enter' == result_list[i][0]:
                    result_list[i][1] = f'{new_username}님이 들어왔습니다.';
                elif f'{id} Leave' == result_list[i][0]:
                    result_list[i][1] = f'{new_username}님이 나갔습니다.';
            
    for i in range(len(result_list)):
        answer.append(result_list[i][1])
        
    return answer;

def solution(record):
    answer = [];
    
    user_info = {};
    
    for rec in record:
        if rec.split(" ")[0] == "Enter" or rec.split(" ")[0] == "Change":
            user_info[rec.split(" ")[1]] = rec.split(" ")[2];
    
    for rec in record:
        if rec.split(" ")[0] == "Enter":
            answer.append(f'{user_info[rec.split(" ")[1]]}님이 들어왔습니다.');
        elif rec.split(" ")[0] == "Leave":
            answer.append(f'{user_info[rec.split(" ")[1]]}님이 나갔습니다.')
        
    return answer