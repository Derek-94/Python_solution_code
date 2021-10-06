class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [];
        def dfs(process, remain_list):
            if len(process) == len(nums):
                result.append(process);
                return;
            
            for index, value in enumerate(remain_list):
                dfs(process + [value], remain_list[:index] + remain_list[index + 1:]);
            
        dfs([], nums);
        return result;