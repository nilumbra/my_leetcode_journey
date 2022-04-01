class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        #if haystack == needle: return 0
        
        hlen = len(haystack)
        nlen = len(needle)
        
        i = 0
        while i <= hlen - nlen:
            if haystack[i: i+nlen] == needle:
                return i
            i += 1
        
        return -1