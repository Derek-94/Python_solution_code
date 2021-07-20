class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified = '';
        for i in s:
            if i.isalnum():
                modified += i.lower();
        return modified == modified[::-1]