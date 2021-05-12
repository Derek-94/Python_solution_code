a, b = map(int, input().strip().split(' '))

tmp = "";
answer = "";

for i in range(b):
    for j in range(a):
        tmp += "*";
    tmp += "\n";
    answer += tmp;
    tmp = "";
    
print(answer)