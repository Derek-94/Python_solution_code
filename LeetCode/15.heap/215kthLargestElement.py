class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1];


class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq;
        
        heapq.heapify(nums);
        
        for _ in range(len(nums) - k):
            heapq.heappop(nums);
        
        return heapq.heappop(nums)