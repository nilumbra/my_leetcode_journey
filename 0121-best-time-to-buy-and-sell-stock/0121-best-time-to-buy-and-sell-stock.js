/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    // Observe that on the i-th day, the best strategy is to buy and sell is to buy at the lowest price and sell at the highest before i-th day. 
    // We can use two variables to store the day of a lowest buy-in and the maximum profit made so far, as we need to scan the entire <prices> to make sure our decision is optimal
    var buy_in = 0,
        max = -Infinity
    
    for (const [idx, p] of prices.entries()) {
        lowest_price = prices[buy_in]
        if (p < lowest_price) {
            buy_in = idx
        } else if (p - lowest_price > max) {
            max = p - lowest_price
        }
    }
    
    return Math.max(max, 0)
};