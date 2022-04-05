/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    
    x = x.toString();
    
    let left = 0,
        right = x.length - 1;
    
    while (left < right) {
        // if x.length % 2 == 0 and x is palindrome, then while loop stops after 
        // left == x.length // 2, right == x.length // 2 + 1
        // if x.length % 2 == 1 and x is palindrome, then while loop stops after 
        // left == x.length // 2 + 1, right == x.length // 2 - 1
        if (x[left] === x[right]){
            left++;
            right--;    
        } else {
            return false
        }
    }
    
    return true
};