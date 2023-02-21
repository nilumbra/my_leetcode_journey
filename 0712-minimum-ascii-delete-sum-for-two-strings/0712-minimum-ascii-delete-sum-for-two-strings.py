class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        #3# Subproblem
        # C(i, j) = lowest ascii sum of deleted characters to make
        #           s1[:i] and s2[:j] equal, 0 <= i < len(s1), 0<= j < len(s2)
        #----------
        #3# Relate
        # C(i, j)
        #----------
        #3# Basecase
        # C(0, 0) = 0
        # C(i, 0) = sum(s1[i])
        # C(0, j) = sum(s2[j])
        #----------
        #3# Original problem
        # C(|s1|, |s2|)
        #----------
        m, n = len(s1), len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][0] = 0
        ascii_sum = 0
        for i in range(m):
          ascii_sum += ord(s1[i])
          dp[i+1][0] = ascii_sum
        
        ascii_sum = 0
        for j in range(n):
          ascii_sum += ord(s2[j])
          dp[0][j+1] = ascii_sum
        # for loop time: O(|s1| * |s2|)
        for i in range(1, m+1):
          for j in range(1, n+1):
            if s1[i-1] == s2[j-1]: # do not have to delete
              dp[i][j] = dp[i-1][j-1]
            else:
              dp[i][j] = min(dp[i-1][j-1] + ord(s1[i-1]) + ord(s2[j-1]),  # delete both
                          dp[i-1][j]   + ord(s1[i-1]), # delete s1[i]
                          dp[i][j-1]   + ord(s2[j-1])) # delete s2[j]    
                                                         
        return dp[m][n]