class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Count the frequency of each letter, increment pa by one whenever a letter reacha even number, and pa * 2 is hence the length of symmetrical letters of the longest palindrome
        Longest palindrome is 
        pa * 2 if pa * 2 == sLen, 
        else pa * 2 + 1
        """
        sLen = len(s)
        pa = 0
        sletM = defaultdict(int)
        for c in s:
            sletM[c] += 1
            if sletM[c] % 2 == 0: pa += 1
                
        
        return pa * 2 if pa * 2 == sLen else pa * 2 + 1