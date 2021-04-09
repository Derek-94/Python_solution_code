n = int(input())
a, b = map(int, input().split())
m = int(input())
 
arr = list([0]*(n) for i in range(n))
v = list([0]*(n))
 
def bfs(x) : 
    
    que = [x]
 
    while que : 
                
        cur = que.pop(0)
               
        for i in range(n) :
 
            if arr[cur][i] == 1 and v[i] == 0 :                
                v[i] = v[cur] + 1
                que.append(i)                   
    
for i in range(m) :
    x, y = map(int, input().split())
    arr[x-1][y-1] = arr[y-1][x-1] = 1
 
bfs(a-1)
 
print(v[b-1] if v[b-1] else -1)