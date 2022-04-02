class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        threshold = 1
        err = 0
        
        def isP(s):
            nonlocal err
            nonlocal threshold
            if len(s) <= 1:
                return True
            else:
                if s[0] == s[-1]:
                    return isP(s[1:-1])
                else:
                    err += 1
                    if err > threshold:
                        return False
                    else:
                        return isP(s[1:]) or isP(s[:-1])
        
        
        return isP(s)
    