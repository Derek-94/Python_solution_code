class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = [];
        def dfs(index, part_sum, chosen):
            if part_sum < 0:
                print(f'over.')
                return;
            if part_sum == 0:
                answer.append(chosen);
                return;
            
            for i in range(index, len(candidates)):
                dfs(i, part_sum - candidates[i], chosen + [candidates[i]]);
        
        dfs(0, target, []);
        return answer;