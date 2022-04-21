/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortByBits = function(arr) {
    
    function count1s(num) {
        var count = 0;
        while (num) {
            num = num & (num - 1);
            count++;
        }
        return count
    }
    
    function compareFunc(a, b) {
        return count1s(a) - count1s(b) || a - b
    }
    
    arr.sort(compareFunc)
    return arr
};