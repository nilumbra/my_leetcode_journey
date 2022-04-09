/**
 * @param {number[]} arr
 * @param {number} start
 * @return {boolean}
 */
var canReach = function(arr, start) {
    
    const seen = new Set()
    
    function dfs(i) {
        seen.add(i)
        var subtreeContains0 = false;
        for (const nei of [i + arr[i], i - arr[i]]) {
            if (arr[nei] == 0) return true
            if (nei >= 0 && nei < arr.length && !seen.has(nei)) {
                subtreeContains0 |= dfs(nei);
            }
        }
        return subtreeContains0
    }
    
    return dfs(start)
};