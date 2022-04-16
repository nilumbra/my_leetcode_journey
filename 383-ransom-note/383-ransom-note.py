from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rD = defaultdict(int)
        for c in ransomNote:
            rD[c] += 1
            
        for c in magazine:
            if c in rD and rD[c] > 0:
                rD[c] -= 1
        
        return 0 == sum(rD.values())
        