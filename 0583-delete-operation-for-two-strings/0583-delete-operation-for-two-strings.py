class Solution:
  def LCS(self, word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    ### topo
    # for i from m-1 to 0: for j from n-1 to 0
    ### basecase
    # dp[M][j] = dp[i][N] = 0
    
    for i in reversed(range(m)):
      for j in reversed(range(n)):
        if word1[i] == word2[j]:
          dp[i][j] = dp[i+1][j+1] + 1
        else:
          dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    
    return dp[0][0]
  
  def minDistance(self, word1: str, word2: str) -> int:
        ## Subproblem
        # M(i, j) = minimum # of step to make word[:i] and word[:j] the same
        ## Original problem
        # M(m, n), where m = len(word1), n = len(word2)
        ## Relate
        # if word1[i] == word2[j]
        #   can have both word1[i], word2[j], no need to delete - M(i, j) = M(i-1, j-1)
        # else
        #   choose to delete the char so as to make the M(i, j) small
    L = self.LCS(word1, word2)
    return len(word1) + len(word2) - 2 * L 
    # Let LCS(word1, word2) = L, the number of delete operation required is 
    # (len(word1) - L) + (len(word2) - L)
     
        