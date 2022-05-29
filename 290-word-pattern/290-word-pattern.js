/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    const m = {},
          fixed = new Set();
    s = s.split(' ');
    if (pattern.length !== s.length) {
        return false;
    }
    
    
    for (const [idx, w] of s.entries()) {
        // If there isn't a mapping yet, assign one
        if (typeof m[pattern[idx]] === 'undefined') {
            if (fixed.has(w)) {
                return false;
            }
            m[pattern[idx]] = w;
            fixed.add(w)
        } else {
            if (m[pattern[idx]] !== w) {
                return false
            }
        }
    }
    
    return true;
};