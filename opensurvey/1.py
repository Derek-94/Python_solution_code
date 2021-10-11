def solution(arr, n):
    answer = False;
    
    arr_map = {};
    for index, ele in enumerate(arr):
        arr_map[ele] = index;
    
    for index, ele in enumerate(arr):
        if n - ele in arr_map and index != arr_map[n - ele]:
            return True;
    
    return answer