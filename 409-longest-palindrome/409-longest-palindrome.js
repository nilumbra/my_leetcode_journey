/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    var getAllRepetitiveLetterPair = function(s) {
        const tab = {}
        for (const c of s) {
            // const k = c.charCodeAt(0);
            if (typeof tab[c] === 'undefined') {
                tab[c] = 1;
            } else {
                tab[c] += 1;
            }
        }    
        return tab;
    }
    
    const t = getAllRepetitiveLetterPair(s);
    // console.log(t)
    var palindromeCnt = 0;
    for (const k in t) {
        const cnt = t[k];
        if (cnt >= 2) {
            palindromeCnt += Math.floor(cnt / 2) * 2;
        }
    }
    
    // console.log(palindromeCnt)
    palindromeCnt += (palindromeCnt < s.length);
    return palindromeCnt
};