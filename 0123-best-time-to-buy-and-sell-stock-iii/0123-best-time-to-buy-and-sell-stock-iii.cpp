class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();
        if (length <= 1) return 0;
        
        int leftMin = prices[0];
        int rightMax = prices[length - 1];
        
        vector<int> p1(length, 0);
        vector<int> p2(length + 1, 0);
        
        // For transaction 1, minimize the buy-in time, solve optimal subproblems in prices[0...i] for 1 <= i <= N - 1
        // For transaction 2, maximize the sell-out time, solve optimal subproblems in prices[i...N-1]for 1 <= i <= N - 1
        for (int l = 1; l < length; ++l){
            p1[l] = max(p1[l - 1], prices[l] - leftMin);
            leftMin = min(prices[l], leftMin);
            
            int r = length - l - 1;
            p2[r] = max(p2[r + 1], rightMax - prices[r]);
            rightMax = max(prices[r], rightMax);
        }
        
        int maxProfit = 0;
        for (int i = 0; i < length; ++i){
            maxProfit = max(maxProfit, p1[i] + p2[i + 1]);
        }
        
        return maxProfit;
    }
};