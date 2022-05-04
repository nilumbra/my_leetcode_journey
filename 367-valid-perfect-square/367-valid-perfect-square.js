/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
  var left = 1,
      right = num;
  while (left < right) {
      let mid = Math.floor((left + right) / 2);
      if (mid * mid > num) {
          right = mid;
      } else if (mid * mid < num) {
          left = mid + 1;
      } else {
          return true
      }
  }
    
  return left * left == num
};