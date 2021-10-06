import itertools;

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = [];
        items = [];
        dics = {'2': 'abc', '3': 'def', '4': 'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9': 'wxyz'};
        
        for digit in digits:
            items.append(list(dics[digit]));
        
        if len(items) == 0:
            return [];
        
        for ele in list(itertools.product(*items)):
            answer.append(''.join(ele));
        
        return answer

class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = [];
        
        process = '';
        dics = {'2': 'abc', '3': 'def', '4': 'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9': 'wxyz'};
        
        def dfs(index, process):
            if len(process) == len(digits):
                answer.append(process);
                return;
            
            for i in range(index, len(digits)):
                for j in dics[digits[i]]:
                    dfs(i + 1, process + j)
        
        if len(digits) == 0:
            return [];
        
        dfs(0, process);
        
        return answer;
            