import heapq;

def solution(n, works):
    answer = 0;
    heap = [];
    
    for work in works:
        heapq.heappush(heap, (-work, work))
    
    while n:
        work = heapq.heappop(heap)[1] - 1
        heapq.heappush(heap, (-work, work))
        n -= 1;

    for i in heap:
        if i[1] < 0:
            continue
        answer += i[1] ** 2
    
    return answer