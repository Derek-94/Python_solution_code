class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap =[];
        
        for x, y in points:
            cal = x ** 2 + y ** 2;
            heapq.heappush(heap, (cal, x, y));
        
        answer = [];
        for _ in range(k):
            distance, x, y = heapq.heappop(heap);
            answer.append([x, y]);
        
        return answer;