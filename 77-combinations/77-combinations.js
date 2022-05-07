/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    let output = [];
    function backtrack(startIndex, curr_combination) {
        if (curr_combination.length === k) {
           output.push(curr_combination);
        } else {
           for (let i = startIndex; i <= n; i++) {
                backtrack(i + 1, curr_combination.concat([i]));
           }
        }
    }
    
    backtrack(1, [])
    return output;
};