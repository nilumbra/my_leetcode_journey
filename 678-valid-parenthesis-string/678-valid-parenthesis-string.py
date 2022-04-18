class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        class ParenthesisChecker():
            def __init__(self, stack=[]):
                self.stack = stack

            def push(self, c):
                if c == "(":
                    self.stack.append(['(', 0])
                elif c == "*":
                    # print(stack)
                    if len(self.stack) == 0 or self.stack[-1] == "*":
                        self.stack.append("*")
                    else:
                        self.stack[-1][1] += 1
                elif c == ")":
                    if self.stack:
                        if self.stack[-1] == "*":
                            self.stack.pop()
                        else:    
                            temp = self.stack.pop()[1]
                            if temp > 0: # pick the '(' out, push all '*' above it to onto the previous stack
                                if len(self.stack) == 0 or self.stack[-1] == "*":
                                    self.stack.extend(['*']*temp)
                                else:
                                    self.stack[-1][1] += temp
                    else:
                        return False

                return True

            def pop(self):
                pass

            def sanity_check(self):
                if len(self.stack) == 0 or self.stack[-1] == "*":
                    return True
                else:
                    # ['(', <some integer>]
                    while self.stack[-1]:
                        if self.stack[-1][1] == 0:
                            return False
                        
                        temp = self.stack.pop()[1]
                        if len(self.stack) == 0 or self.stack[-1] == "*": 
                            return True
                        else:
                            self.stack[-1][1] += temp - 1
                            

                    return True
                    
        pchecker = ParenthesisChecker()
        for c in s:
            if not pchecker.push(c):
                return False
        
        print(pchecker.stack)
        return pchecker.sanity_check()