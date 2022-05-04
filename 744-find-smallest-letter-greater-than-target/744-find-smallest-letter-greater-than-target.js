/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
var nextGreatestLetter = function(letters, target) {
    var left = 0,
        right = letters.length;
    
    while (left < right) {
        let mid = Math.floor((left + right) / 2);
        if (letters[mid] > target) {
            right = mid;
        } else {
            left = mid + 1
        }
    }
    
    return left === letters.length ? letters[0] : letters[left]
};