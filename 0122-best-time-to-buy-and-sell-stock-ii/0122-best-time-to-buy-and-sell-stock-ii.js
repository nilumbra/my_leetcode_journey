/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    var total = 0,
        currProfit = 0;
    const diff = (beforePrice, afterPrice) => afterPrice - beforePrice;
    
    for (let i = 1; i < prices.length; ++i) {
        let d = diff(prices[i - 1], prices[i]);
        
        if(d < 0) {
            total += currProfit;
            currProfit = 0;
        } else {
            currProfit += d;
        }
        
        // console.log(`${d} ${currProfit} ${total}`)
    }
    
    total += currProfit;
    
    return total;
};