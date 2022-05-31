/**
 * @param {string} s
 * @return {number[]}
 */
var partitionLabels = function(s) {
    const last = {};
    const charArr = s.split('');
    charArr.forEach((c, i) => { last[c] = i; });
    
    var start = end = 0;
    
    const ans = []
    for (const [i, c] of charArr.entries()) {
        end = Math.max(end, last[c]);
        if (i == end){
            ans.push((i+1) - start);
            start = i + 1;
        }
    }
    
    return ans;
};