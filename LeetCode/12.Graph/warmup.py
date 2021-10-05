graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}

def recursiveBFS(v, visited=[]):
    visited.append(v);
    for w in graph[v]:
        if w not in visited:
            visited = recursiveBFS(w, visited);

    return visited;

def stackBFS(v):
    stack = [];
    visited = [];
    stack.append(v);

    while stack:
        nextV = stack.pop();
        if nextV not in visited:
            visited.append(nextV);
            for others in graph[nextV]:
                stack.append(others);
    return visited;

print(recursiveBFS(1));
print(stackBFS(1));