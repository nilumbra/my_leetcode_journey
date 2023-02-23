class Solution {
public:
    int minDistance(string word1, string word2) {
        // ###subproblem
        // dp[i][j] = the edit distance between word1[i:] and word2[j:], 0 <= i <= |word1|, 0 <= j <= |word2|
        //
        // ### Relate
        // dp[i][j] = dp[i+1][j+1] if word1[i] == word2[j]
        // dp[i][j] = min( dp[i+1][j+1],  #replace
        //                 dp[i+1][j],    #  word1 insert / delete
        //                 dp[i][j+1],    #  word2 insert / delete
        //               )
        // ### Basecase
        // dp[|word1|][j] = |word2| - j
        // dp[i][|word2|] = |word1| - i
        //
        // ### Original problem
        // dp[0][0] := edit distance between word1[0:] and word2[0:] 
        int m = word1.length();
        int n = word2.length();
        
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        for (int i = 0; i < m; i++) {
          dp[i][n] = m - i;
        }   
        for (int j = 0; j < n; j++) {
          dp[m][j] = n - j;
        }   
      
        for (int i = m - 1; i >= 0; i--) {
          for (int j = n - 1; j >= 0; j--) {
            if(word1[i] == word2[j]) dp[i][j] = dp[i+1][j+1];
            else {
              dp[i][j] = min(min(dp[i+1][j+1], dp[i+1][j]), dp[i][j+1]) + 1;
            }
          }
        }
      
      
        return dp[0][0];
    }
};