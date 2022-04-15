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
    var last_p = coordinates[1];
    for (const p of coordinates.slice(2)) {
        // console.log(`${last_p}, ${p}, ${diff2d(last_p, p)}, ${fixed}`)
        if (k(p, last_p) != slope) return false
        last_p = p
    }
    return true
};