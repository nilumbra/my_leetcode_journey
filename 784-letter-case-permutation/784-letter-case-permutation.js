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
            upper_lower_variations(s[i]).forEach(c => {
                backtrack(i + 1, curr + c)
            })
        }
    }
    
    const out = [];
    backtrack(0, "")
    
    return out
};