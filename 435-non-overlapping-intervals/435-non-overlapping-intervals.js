/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function(intervals) {
    intervals.sort((a, b) => (a[1] - b[1]));
    var removeCnt = 0,
        prevLast = -Infinity;
    
    for (const interval of intervals) {
        if (interval[0] >= prevLast) { // e.g. prevLast: 10, interval: [11, 13]
            prevLast = interval[1]
            // console.log(interval, "no remove")
        } else {
            // e.g. prevLast: 10, interval: [9, 13]
            // console.log(interval, "remove")
            removeCnt++;  
        }
        
        // console.log(prevLast)
    }
    
    return removeCnt;
};