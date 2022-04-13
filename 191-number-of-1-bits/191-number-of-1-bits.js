/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    const mask = 1;
    var count = 0;
        
    for (let i = 0; i < 32; i++) {
        if (n & mask == 1) count++
        n = n >> 1;
    }
    
    return count;
};