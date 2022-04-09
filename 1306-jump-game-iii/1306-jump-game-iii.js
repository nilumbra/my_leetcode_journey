/**
 * @param {number[]} arr
 * @param {number} start
 * @return {boolean}
 */
var canReach = function(arr, start) {
    if (start >= 0 && start < arr.length && arr[start] >= 0) {
        if (arr[start] == 0) return true
        
        arr[start] = -arr[start]
        return canReach(arr, start + arr[start]) || canReach(arr, start - arr[start])
        
    }
    return false
};