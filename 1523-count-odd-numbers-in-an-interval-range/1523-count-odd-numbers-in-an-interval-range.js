/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds = function(low, high) {
    // Low is odd, high is odd. e.g. low = 3, high = 7, i.e. [3, 5, 7] numOfinBetweenOdd = (high - low) / 2 + 1, 
    // Low is odd, high is even. e.g. low = 3, high = 8, i.e. [3, 5, 7], numOfinBetweenOdd = (high- low  + 1 ) / 2 , 
    // Low is even, high is odd. e.g. low = 4, high = 9, i.e. [5, 7, 9], numOfinBetweenOdd = (high - low + 1) / 2 , 
    // low = 4, high = 10, i.e. [5, 7, 9]
    
    if ((low + high) % 2 == 1) return (high - low + 1) / 2
    if (low % 2 == 0 && high % 2 == 0) return (high - low) / 2
    if (low % 2 == 1 && high % 2 == 1) return (high - low) / 2 + 1
    
};