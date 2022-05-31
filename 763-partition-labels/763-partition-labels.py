def isP(letterCnt, L):
    for c in L:
        if letterCnt[c] > 0:
            return False
    
    return True

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterCnt = [0] * 26
        for c in s:
            letterCnt[ord(c) - 97] += 1
        
        left = 0
        right = 1
        
        L = set()
        ans = []
        part = 0
        for idx, c in enumerate(s):
            ccode = ord(c) - 97
            L.add(ccode)
            part += 1
            letterCnt[ccode] -= 1
            if isP(letterCnt, L):
                ans.append(part)
                L.clear()
                part = 0
        
        return ans
    