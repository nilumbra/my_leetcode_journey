class Solution:
    def calculate(self, s: str) -> int:
        def tokenize(s):
            """
            returns: 
                AST represented using nested list
            """
            tklist = []
            
            l = len(s)
            i = 0
            while i < l:
                if s[i] in ['(', ')', '-', '+']:
                    tklist.append(s[i])
                elif s[i].isdigit(): # digit
                    j = i
                    while j < l and s[j].isdigit():
                        j += 1
                    tklist.append(int(s[i:j]))
                    i = j - 1
                
                i += 1
                
            return tklist
        
        def parse(s):
            """
            returns: 
                AST represented using nested list
            """
            pass
        
        def e(evSt):
            """
            evaluetes:
                e = - NUM | NUM + NUM | NUM - NUM
            """
            if len(evSt) >= 2:
                num = evSt.pop()
                if evSt[-1] == '+': # can assume len(evSt) > 3 when having a preceding '+'                      
                    evSt.pop()
                    evSt[-1] += num
                else: # '-'
                    evSt.pop()
                    if len(evSt) > 0 and isinstance(evSt[-1], int):
                        evSt[-1] -= num
                    else:
                        # print(num)
                        evSt.append(-num)                
            
        def evaluate(tklist) -> int:
            """
            """
            evSt = []
            for tk in tklist:
                # print(evSt)
                if tk != ')':
                    evSt.append(tk)
                    if len(evSt) > 1 and isinstance(tk, int) and evSt[-2] in ['+', '-']: 
                        e(evSt) 
                else: # ')'
                    num = evSt.pop()
                    evSt.pop() # pop() must be '('
                    evSt.append(num)
                    if len(evSt) > 1 and evSt[-2] in ['+', '-']:
                        e(evSt)
            return evSt
        
#         print("tokens:")
#         print(tokenize(s))
        
#         print(evaluate(tokenize(s)))
        
        
        return evaluate(tokenize(s))[0]
        