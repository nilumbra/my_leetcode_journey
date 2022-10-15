class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        
        nh, h = 0, -float('inf')
        for i in range(n):
            nh, h = max(nh, h + prices[i]), max(h, nh - prices[i] - fee)    
        
        return nh