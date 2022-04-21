/**
 * @param {string} s
 * @return {string[]}
 */
var letterCasePermutation = function(s) {
    function upper_lower_variations(c){
        const i = c.charCodeAt(0)
        return 48 <= i && i <= 57 ? [c] : [c.toLowerCase(), c.toUpperCase()]
    }
    
    function backtrack(first, curr) {
        if (curr.length == s.length) {
            out.push(curr)
        }
        
        for (let i = first; i < s.length; i++) {
            const lCase = s[i].toLowerCase(),
                  uCase = s[i].toUpperCase();
            
            if (lCase == uCase) {
                backtrack(i + 1, curr + s[i])
            } else {
                backtrack(i + 1, curr + lCase)
                backtrack(i + 1, curr + uCase)
            }
        }
    }
    
    const out = [];
    backtrack(0, "")
    
    return out
};