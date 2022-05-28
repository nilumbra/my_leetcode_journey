
function addTwoDigits(a, b) {
    var carry;
    if ((a + b) >= 10) {
        carry = 1;
    } else {
        carry = 0
    }
    
    return [(a + b) % 10, carry];
}
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
    var d1, d2, carry, curr;
    // reading both num1 and num2 from right to left -> d1, d2 
    // So the places increase from 10 ** 0, 10 ** 1, 10 ** 2, ...
    // d1 + d2
    
    const l = Math.max(num1.length, num2.length);
    
    const ans = [];
    carry = 0;
    for (let i = 0; i < l; i++) {
        d1 = num1.at(-1 - i);
        d2 = num2.at(-1 - i);
        d1 = typeof d1 !== 'undefined'? parseInt(d1) : 0;
        d2 = typeof d2 !== 'undefined'? parseInt(d2) : 0;
        
        
        [curr, nxt_carry] = addTwoDigits(d1, d2);
        // console.log(curr, nxt_carry);
        
        curr += carry;
        if (curr == 10) {
            nxt_carry = 1;
            ans.unshift('' + 0);
        } else {
            ans.unshift('' + curr);    
        }
        
        carry = nxt_carry;
        // console.log(ans);
    }
    
    if (carry !== 0) {
        ans.unshift('' + carry);
    }
    
    return ans.join("");
};