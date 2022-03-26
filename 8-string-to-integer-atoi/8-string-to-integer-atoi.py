import re
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1 
        
        num = ["0"]
        sign = 1
        # index on first non whitespace character
        if i < len(s):
            if s[i] in {'+', '-'}:
                sign = 1 if s[i] == '+' else - 1
                i += 1
        
        while i < len(s) and s[i].isnumeric():
            num.append(s[i])
            i += 1
        
        num = ''.join(num)
        if int(num) == 0: return 0
        num = int(num.lstrip('0')) * sign
        
        return max(-2**31, min(num, 2**31 - 1))