class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand1(left: int, right: int, s: str):
            # print('left', left, 'right: ', right)
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1;
                right += 1;
            return s[left+1:right];
        
        if len(s) < 2 or s == s[::-1]:
            return s;
        result = '';
        for i in range(len(s)):
            result = max(result, expand1(i, i+1, s), expand1(i, i+2, s), key = lambda x: len(x));
        return result;