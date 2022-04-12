/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const mem = new Set();
    
    var dup = false;
    for (const num of nums) {
        if (!mem.has(num)){
            mem.add(num)
        } else {
            return true
        }
    }
    return false
};