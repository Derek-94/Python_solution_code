class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {};
        for key, value in enumerate(nums):
            if target - value in hash_map:
                return [key, hash_map[target - value]];
            hash_map[value] = key;