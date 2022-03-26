class Solution:
    def isValid(self, s: str) -> bool:
        reg = []
        bracket_set = {')' : '(', ']':'[', '}': '{'}
        for c in s:
            if c in {'(', '[', '{',}:
                reg.append(c)
            if c in {')', ']', '}',}:
                if len(reg) == 0: return False
                if reg[-1] == bracket_set[c]:
                    reg.pop()
                else:
                    return False
        
        return True if len(reg) == 0 else False