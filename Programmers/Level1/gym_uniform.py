def borrow(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            if i == 0:
                if arr[i + 1] == 2:
                    arr[i] += 1;
                    arr[i + 1] -= 1;
            elif i == len(arr) - 1:
                if arr[i - 1] == 2:
                    arr[i] += 1;
                    arr[i - 1] -= 1;
            else:
                if arr[i - 1] == 2:
                    arr[i] += 1;
                    arr[i - 1] -= 1;
                elif arr[i + 1] == 2:
                    arr[i] += 1;
                    arr[i + 1] -= 1;
    
    return arr;
            
            

def solution(n, lost, reserve):
    answer = 0;
    students = [1 for i in range(n)];
    
    for index in lost:
        students[index - 1] -= 1;
    for index in reserve:
        students[index - 1] += 1;
    
    students = borrow(students);
    
    for val in students:
        if val != 0:
            answer += 1;
    
    return answer;