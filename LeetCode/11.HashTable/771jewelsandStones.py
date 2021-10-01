import collections;

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0;
        
        dic = collections.defaultdict(int);
        
        for stone in stones:
            dic[stone] += 1;
                
        for jewel in jewels:
            count += dic[jewel];
        
        return count

class Solution1:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0;
        counter = collections.Counter(stones);
        
        for jewel in jewels:
            count += counter[jewel];
        
        return count;

class Solution3:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones);