/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    const [m, n] = [matrix.length, matrix[0].length];
    var [i, j] = [matrix.length - 1, 0];
    
    const isValidIndex = (i, j) => (i >= 0 && j >= 0 &&
                                    i < m && j < n);
    
    while (isValidIndex(i, j)) {
        if (matrix[i][j] > target) { 
            // Because everything to the right of (i,j) is greater than <target>,
            // we have no choice but go up;
            i--;
        } else if (matrix[i][j] < target) {
            // search righthand side
            j++;
        } else { // eq
            return true;
        }
    }
    return false;
};
