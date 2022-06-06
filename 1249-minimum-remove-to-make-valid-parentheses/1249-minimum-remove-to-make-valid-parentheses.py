def checkBalance(s):
    """
    Params
    -------
    s: str
    
    Do
    -------
    Calculate balance and delete any invalid ')' on the go
    
    Returns
    -------
    tuple
        (pre, balance)
    """
    
    pre = []
    balance = 0
    
    for c in s: 
        if c == ')':
            if balance == 0: 
                # do not append an invalid ')' to pre or decrement balance
                continue
            balance -= 1
            
        elif c == '(':
            balance += 1
        
        pre.append(c)
            
    return (pre, balance)


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s, balance = checkBalance(s)
        # print(s, balance)
        if balance <= 0: # No superfluous left parenthesis left
            return ''.join(s)
        else: # Need to delete superfluous left parenthesis
            res = []
            for c in s[::-1]:
                if balance > 0 and c == '(':
                    # skip
                    balance -= 1
                    continue
                
                res.append(c)
                
            return ''.join(res[::-1])
                
                