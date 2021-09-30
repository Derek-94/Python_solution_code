class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures);
        stack = [];
        
        for index, t in enumerate(temperatures):
            print(f'==={index}th turn, and the value is {t}===');
            
            while stack and t > temperatures[stack[-1]]:
                target = stack.pop();
                answer[target] = index - target;
            
            stack.append(index);
        return answer;
            