class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        u, l = 90, 65
        ans = []
        for c in s:
            if l <= ord(c) <= u:
                ans.append(chr(ord(c) + 32))
            else:
                ans.append(c)
        
        return ''.join(ans)