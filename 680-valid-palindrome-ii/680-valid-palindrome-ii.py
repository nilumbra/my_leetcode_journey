class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        def isP(s, i, j):
            while(i < j):
                if(s[i] != s[j]):
                    return False
                i += 1
                j -= 1
            
            return True
        
        left, right = 0, len(s) - 1
        # threshold = 1
        # err = 0
        while left < right:
            if (s[left] == s[right]):
                left += 1
                right -= 1
            else:
                return isP(s, left+1, right) or isP(s, left, right-1)
            
        return True
        
#         def isP(s):
#             nonlocal err
#             nonlocal threshold
#             if len(s) <= 1:
#                 return True
#             else:
#                 if s[0] == s[-1]:
#                     return isP(s[1:-1])
#                 else:
#                     err += 1
#                     if err > threshold:
#                         return False
#                     else:
#                         return isP(s[1:]) or isP(s[:-1])
        
    
    