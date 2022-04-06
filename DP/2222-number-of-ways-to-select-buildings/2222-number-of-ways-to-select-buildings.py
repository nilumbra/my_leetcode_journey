class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """

        n0 = 0
        n01 = 0
        n010 = 0
        
        for i in range(2, len(s)):
            n0 += 1 if s[i-2] == '0' else 0
            n01 = n01 if s[i-1] == '0' else n0 + n01  # n01[i-1] 
            n010 = n010 if s[i] == '1' else n01 + n010
            
        n1 = 0
        n10 = 0
        n101 = 0
        for j in range(2, len(s)):
            n1 += 1 if s[j-2] == '1' else 0
            n10 = n10 if s[j-1] == '1' else n1 + n10  # n01[i-1] 
            n101 = n101 if s[j] == '0' else n10 + n101
            
        return n010 + n101
        
        