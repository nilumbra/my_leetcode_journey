# from collections import defaultdict
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        maxLen = 1
        dp = {}
        for num in arr:
            if num - difference not in dp:
                dp[num] = 1              
            else:
                dp[num] = dp[num - difference] + 1
                maxLen = max(maxLen, dp[num])
        return maxLen
        