/**
 * @param {string} s
 * @return {string[]}
 */
var findRepeatedDnaSequences = function(s) {
    var seq10, ans;
    if (s.length <= 10) {
        return [];
    }  else {
        seq10 = new Set();
        ans = new Set();
        for (let i = 0; i <= s.length - 10; i++) {
            const seq = s.slice(i, i + 10);
            if (!seq10.has(seq)) {
                seq10.add(seq);
            } else {
                ans.add(seq);
            }
        }
    }
    
    return Array.from(ans);
};