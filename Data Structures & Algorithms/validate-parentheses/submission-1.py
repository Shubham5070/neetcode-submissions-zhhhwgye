class Solution:
    def isValid(self, s: str) -> bool:
        check = {'{': '}', '(': ')', '[': ']'}
        x = []

        for i in range(len(s)):
            if s[i] in check:
                x.append(s[i])
            else:
                if not x:
                    return False
                m = x.pop()
                if check[m] != s[i]:
                    return False
        
        return len(x) == 0