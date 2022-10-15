class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0, 0] for j in range(k + 1)] for i in range(n)]
        # for j in range(k):
        #     dp[0][j][1] = float(-inf)
        
        # print(f'dim(dp)=({len(dp)}, {len(dp[0])}, {len(dp[0][0])})')
        # print(dp[3][1][0])
        
        for i in range(n):
            for j in range(k + 1):
                if i - 1 == -1:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                if j - 1 == -1:
                    dp[i][j][1] = -prices[i]
                    continue
                # print(i, j)
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        # print(n+1, k+1)
        return dp[n - 1][k][0]