class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        # memo[len(word1), len(word2)] = 0
        def recurrence(i, j):
            if (i, j) not in memo:
                if (i, j) == (len(word1), len(word2)):
                    ans = 0
                elif i == len(word1):
                    ans = len(word2) - j
                elif j == len(word2):
                    ans = len(word1) - i

                # if the first character of two suffices is identical
                elif word1[i] == word2[j]:
                    ans = min(recurrence(i+1, j) + 1, # insert word1[i] before word1[j+1:]
                              recurrence(i, j+1) + 1, # delete word2[j] from word2[j:]
                              recurrence(i+1, j+1)) # no change required
                else:
                    ans = 1 + min(recurrence(i+1, j), # insert word1[i] before word1[j+1:]
                                  recurrence(i, j+1), # delete word2[j] from word2[j:]
                                  recurrence(i+1, j+1)) # no change required
                
                memo[i, j] = ans
            print(memo)
            return memo[i, j]
        
        return recurrence(0, 0)
        
    def minDistance_bottom_up(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        if n * m == 0: # if one of the strings is empty
            return n + m

        dp = [[0] * (m + 1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][m] = n - i

        for j in range(m+1):
            dp[n][j] = m - j

        for i in reversed(range(n)):
            for j in reversed(range(m)):
                down = dp[i+1][j]
                right = dp[i][j+1]
                diag = dp[i+1][j+1]

                if (word1[i] == word2[j]):
                    dp[i][j] = min(down + 1, right + 1, diag)
                else:
                    dp[i][j] = min(down, right, diag) + 1


        return dp[0][0]

        
if __name__ == '__main__':
    solution = Solution()
    # print(solution.minDistance("intention", "execution"))
    print(solution.minDistance_bottom_up("horse", "ros"))