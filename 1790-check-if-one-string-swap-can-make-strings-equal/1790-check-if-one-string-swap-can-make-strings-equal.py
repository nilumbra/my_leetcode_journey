class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        dfcount = 0
        s = ""
        
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            else:
                dfcount += 1
                if dfcount == 1:
                    s = s1[i] + s2[i]
                if dfcount == 2:
                    if s2[i] + s1[i] == s:
                        continue
                    else:
                        return False
                
                if dfcount > 2: return False
        
        return dfcount in {0, 2}
            