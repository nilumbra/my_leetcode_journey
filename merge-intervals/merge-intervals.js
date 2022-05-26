/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals.sort((a, b) => a[0] - b[0]);

    const ans = [intervals[0]];
    for (const interval of intervals.slice(1)) {
        let last_interval = ans.at(-1)
        if (interval[0] <= last_interval[1]) {  // overlapping        
            if (interval[1] > last_interval[1]) {
                // e.g. last_interval = [1, 3], interval = [2, 6]
                last_interval[1] = interval[1];
            } 
            
           // e.g. last_interval = [1, 4], interval = [2, 3] ...
           // Do nothing
        } else {
            ans.push(interval)
        }
    }

    return ans;
};