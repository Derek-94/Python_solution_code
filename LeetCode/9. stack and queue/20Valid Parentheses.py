class Solution:
    def isValid(self, s: str) -> bool:
        stack = [];
        
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for p in s:
            if p not in table:
                stack.append(p);
            elif not stack or table[p] != stack.pop():
                return False;
        
        return len(stack) == 0;