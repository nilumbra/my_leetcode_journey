/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortByBits = function(arr) {
    
    function count1s(num) {
        var count = 0;
        while (num) {
            if (num & 1) count++;
            num >>= 1
        }
        return count
    }
    
    function compareFunc(a, b) {
        // return > 0, sort b before a
        const bitDiff = count1s(a) - count1s(b)
        if (bitDiff != 0) {
            return bitDiff
        } else {
            return a - b
        }
    }
    
    arr.sort(compareFunc)
    return arr
};