class Solution {
public:
    int maxProfit(vector<int>& prices) {
       int sold = INT_MIN,
           held = INT_MIN,
          reset = 0;
       for (int price : prices) {
           // we are gonna modify sold's value first
           // so need to cache sold's value before change
           int _sold = sold; 
           
           sold = held + price; // 
           held = max(held, reset - price);
          reset = max(_sold, reset);
       }
       
       return max(sold, reset);
    }
};