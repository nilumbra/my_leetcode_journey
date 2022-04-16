class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charindex = [-1] * 128
        longest = 0
        left = 0
        
        for i, c in enumerate(s):
            # print(left, i, longest)
            last_occu = charindex[ord(c)]
            if  last_occu == -1 or last_occu < left: # if first appearance of c
                longest = max(longest, i - left + 1)
            else:
                left = last_occu + 1
                
            charindex[ord(c)] = i
        
        
        return longest