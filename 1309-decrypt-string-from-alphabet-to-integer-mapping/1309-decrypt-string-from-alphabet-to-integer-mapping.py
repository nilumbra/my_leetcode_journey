class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        def i_to_c(i):
            if len(i) == 3:
                i = i[:2]
                return chr(int(i) + 96)
            else:
                return chr(int(i) + 96)
                
           
        ans = ""
        chang = len(s)
        i = 0
        while i < chang:
            if i + 2 <= chang - 1 and s[i + 2] == '#':
                ans += i_to_c(s[i: i + 3])
                i += 3
            else:
                ans += i_to_c(s[i])
                i += 1
        
        return ans
        
        