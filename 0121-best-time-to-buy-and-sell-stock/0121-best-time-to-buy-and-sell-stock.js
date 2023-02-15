/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    // Observe that on the i-th day, the best strategy is to buy and sell is to buy at the lowest price and sell at the highest before i-th day. 
    // We can use two variables to store the day of a lowest buy-in and the maximum profit made so far, as we need to scan the entire <prices> to make sure our decision is optimal
  
//     var cumulative = 0,
//         m = -Infinity;
//     const diff = (beforePrice, afterPrice) => afterPrice - beforePrice;
    
    
//     for (let i = 1; i < prices.length; ++i) {
//         let d = diff(prices[i - 1], prices[i]);
        
//         if (d + cumulative < 0) cumulative = 0;
//         else cumulative += d;
        
//         m = Math.max(m, cumulative);
//         // console.log(`${m}, ${cumulative}`)
//     }
  
  var max_profit = -1
  var min_price = Infinity
  for (let p of prices) {
    max_profit = Math.max(p - min_price, max_profit)
    if (p < min_price)
      min_price = p
  }

  // code goes here  
  return Math.max(max_profit, 0)
};