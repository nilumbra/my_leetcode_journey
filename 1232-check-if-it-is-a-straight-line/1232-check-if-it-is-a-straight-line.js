/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */
var checkStraightLine = function(coordinates) {
    coordinates.sort()
    console.log(coordinates)
    const k = (p2, p1) => (p2[1] - p1[1]) / (p2[0] - p1[0]),
          slope = k(coordinates[1], coordinates[0]);
    // console.log(hor_ver)
    for (let i = 2; i < coordinates.length; i++) {
        // console.log(`${last_p}, ${p}, ${diff2d(last_p, p)}, ${fixed}`)
        if (k(coordinates[i], coordinates[i-1]) != slope) return false
    }
    return true
};