import math;

class reversor:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return other.obj == self.obj

    def __lt__(self, other):
        return other.obj < self.obj

def cal_distance(x, y):
    return (x**2) + (y**2);

def solution(names, homes, grades):
    answer = [];
    
    order = [];
    dict = {};
    
    if len(names) == 1:
        return [1];
    
    for i in range(len(names)):
        x, y = homes[i]
        order.append((names[i], cal_distance(x, y), math.floor(grades[i])));
    
    order.sort(reverse=True, key=lambda x: (x[2], x[1], reversor(x[0])));
    
    for i in range(len(names)):
        name, d, s = order[i];
        dict[name] = i + 1;
        
    for i in range(len(names)):
        answer.append(dict[names[i]]);

    return answer