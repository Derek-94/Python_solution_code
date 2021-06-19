import collections;

def bfs(start, adj, visited, n):
    que = collections.deque();
    que.append(start);
    while que:
        target = que.popleft();
        for edge in adj[target]:
            if visited[edge] == 0:
                visited[edge] = visited[target] + 1;
                que.append(edge);

def solution(n, edge):
    answer = 0;
    #graph = [[0] * n for _ in range(n)];
    adj = [[] for _ in range(n)]
    for e in edge:
        x = e[0] - 1;
        y = e[1] - 1;
        adj[x].append(y)
        adj[y].append(x)
    visited = [0 for _ in range(n)];
    
    # for ver in edge:
    #     graph[ver[0] - 1][ver[1] - 1] = 1;
    #     graph[ver[1] - 1][ver[0] - 1] = 1;
    
    visited[0] = 1;
    bfs(0, adj, visited, n);
    
    max_value = max(visited);
    answer = visited.count(max_value)
            
    return answer