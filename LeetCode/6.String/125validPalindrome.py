class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified = '';
        for i in s:
            if i.isalnum():
                modified += i.lower();
        
        '''
        Using regex...
        s = s.lower();
        m = re.sub('[^0-9a-z]', '', s);
        print(m[::-1] == m)
        '''
        
        return modified == modified[::-1]