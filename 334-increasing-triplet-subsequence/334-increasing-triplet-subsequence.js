/**
 * @param {number[]} nums
 * @return {boolean}
 */


// If curr element is greater than the last, append
// else if it is smaller than the last one, 


var increasingTriplet = function(nums) {
    var first = Infinity,
        second = Infinity;
    
    for (const num of nums) {
        if (num <= first) {
            first = num;
        } else if (num <= second) {
            second = num;
        } else {
            return true
        }
        
        // console.log(first, second)
    }
    
    return false;
};