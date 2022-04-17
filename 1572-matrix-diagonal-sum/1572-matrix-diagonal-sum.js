/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    const size = mat.length;
    var sum = 0;
    
        for (let i = 0; i < size; i++) {
            sum += mat[i][i]
        }
        for (let i = 0; i < size; i++) {
            sum += mat[i][size - 1 - i]
        }
    
    if (size % 2 == 1) {
        const m = Math.floor(size / 2);
        sum -= mat[m][m]
    }
    
    return sum
};