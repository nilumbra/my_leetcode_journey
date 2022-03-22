class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) == len(t):  # same length 
            if s == t:
                return False
            diff = 0
            for i in range(len(s)):
                if(s[i] != t[i]): diff += 1
                if diff > 1: return False
            return True
            
        else: # different length; do deletion
            if abs(len(s) - len(t)) != 1: 
                return False
            else: # diff of len == 1
                if s in t or t in s:
                    return True
                else:
                    m, n  = len(s), len(t)
                    l = min(m, n)
                    diff = 0 
                    for i in range(l):
                        # print(i)
                        if(s[i] != t[i]):
                            if(m > n):
                                s = s[:i] + s[i+1:]
                            else:
                                t = t[:i] + t[i+1:]
                            diff += 1
                        
                        if(diff > 1): return False
                    
                    return True if s == t else False
                
    def one_pass_with_less_code(self, s: str, t: str) -> bool:
        slen, tlen = len(s), len(t)

        # Always have s be shorter than t
        if (slen > tlen):
            return self.one_pass_with_less_code(t, s)

        # If t is longer than s by more than 1, then it is impossible to make two strings the same by only one edit
        if nt - ns > 1:
            return False

        # For special cases where s is a substring of t with 1 character short 
        if s in t:
            return True 

        for i in range(ns):
            if (s[i] != t[i]):
                if(ns == nt):
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i:] == t[i+1:]
