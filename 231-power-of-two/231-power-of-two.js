/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    return n <= 0 ? 0 : !(n & (n - 1))
};