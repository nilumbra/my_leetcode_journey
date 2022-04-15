/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    // First column is sorted
    // Binsearch on first column, pick the previously smaller one
    const m = matrix.length,
          n = matrix[0].length;
    
    var left = 0,
        right = m - 1;
    
    if (m > 1){
        while (left <= right) {
            let pivot = Math.floor((right + left) / 2);
            if (matrix[pivot][0] == target) return true
            if (matrix[pivot][0] > target) {
                right = pivot - 1;
            } else {
                left = pivot + 1;
            }
        }
        console.log(`Target is in ${left - 1}, if exists.`)

        // Each row is sorted
        // Binsearch to find
    }
    
    var targetRow = m > 1 ? matrix[Math.max(left - 1, 0)]:  matrix[0]
    console.log(m > 1 )
        
    var left = 0,
        right = n - 1;
    
    while (left <= right) {
        let pivot = Math.floor((right + left) / 2);
        if (targetRow[pivot] == target) return true
        if (targetRow[pivot] > target) {
            right = pivot - 1;
        } else {
            left = pivot + 1;
        }
        // console.log(`${left}:${right}`)
    }
    return false
};