/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
  if (nums.length == 1) return nums[0]
    
  var left = right = 0,
      best_sum = -Infinity,
      curr_sum = 0; // sum(nums.slice(left, right + 1))
    
    for (const [idx, num] of nums.entries()) {
        curr_sum += num;
        if (curr_sum > best_sum) {
            right++;
            best_sum = curr_sum
        } 
        if (curr_sum < 0) {
            curr_sum = 0;
            left = right = idx + 1;
        }   
    }
    
    return best_sum
};