import heapq;

def solution(scoville, K):
    answer = 0;
    
    heapq.heapify(scoville);
    
    while scoville[0] <= K:
        if len(scoville) < 2:
            answer = -1;
            break;
        min_spicy = heapq.heappop(scoville);
        next_min_spicy = heapq.heappop(scoville);
        mixed = min_spicy + (next_min_spicy * 2);
        heapq.heappush(scoville, mixed);
        answer += 1;
    
    return answer