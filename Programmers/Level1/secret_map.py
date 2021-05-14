def transfer(target, std):
    result = "";
    while target >= 1:
        target, remain = divmod(target, 2);
        result += str(remain);
    
    while len(result) < std:
        result += "0";
    return result[::-1];
    

def solution(n, arr1, arr2):
    answer = [];
    arr1_transfer = [];
    arr2_transfer = [];
    
    for i in range(n):
        arr1_transfer.append(transfer(arr1[i], n));
        arr2_transfer.append(transfer(arr2[i], n));
    
    for y in range(n):
        tmp = "";
        for x in range(n):
            if arr1_transfer[y][x] == '1' or arr2_transfer[y][x] == '1':
                tmp += "#";
            else:
                tmp += " ";
        answer.append(tmp)
        
    
    return answer