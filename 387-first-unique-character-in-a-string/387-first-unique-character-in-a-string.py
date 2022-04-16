class Solution:
    def firstUniqChar(self, s: str) -> int:
        repc = {}
        for i, c in enumerate(s):
            if c not in repc:
                repc[c] = i
            else:
                repc[c] = -1
        
        funiq = -1
        for v in repc.values():
            if v != -1:
                return v
            
        return -1
                
                