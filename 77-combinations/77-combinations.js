/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    let output = [];
    function backtrack(startIndex, curr_combination) {
        if (curr_combination.length === k) {
           output.push(curr_combination.slice());
        } else {
           for (let i = startIndex; i <= n; i++) {
                curr_combination.push(i)
                backtrack(i + 1, curr_combination);
                curr_combination.pop()
           }
        }
    }
    
    backtrack(1, [])
    return output;
};