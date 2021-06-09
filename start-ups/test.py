def twoSum(nums, target):
    nums_map = {};
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i];
        nums_map[num] = i;

print(twoSum([2,7, 11, 15], 26))