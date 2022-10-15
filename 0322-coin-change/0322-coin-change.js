/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    const memo = {};
    coins.sort((a, b) => a - b);
    var minCoins = function(amount) {
        if (amount === 0) return 0;
        if (amount < 0) return -1;
        if (amount in memo) return memo[amount];
        
        var ans = Infinity;
        for (const coin of coins) {
            let res = minCoins(amount - coin);
            if (res === -1) continue;
            
            ans = Math.min(ans, res);
        }
        if (ans === Infinity)
            return memo[amount] = -1;
        else 
            return memo[amount] = ans + 1
    }
    
    return minCoins(amount);
};


